"""
Local Database Handler for Simple Saver Bot
Replaces Firebase with local JSON file storage
"""

import json
import os
import threading
from pathlib import Path
from typing import Any, Dict, Optional

class LocalDatabase:
    """Simple local JSON-based database to replace Firebase"""
    
    def __init__(self, base_path: str = "database"):
        self.base_path = Path(base_path)
        self.base_path.mkdir(parents=True, exist_ok=True)
        self._cache = {}
        self._lock = threading.Lock()
        self._load_cache()
    
    def _get_file_path(self, path: str) -> Path:
        """Convert database path to file path"""
        # Remove leading/trailing slashes
        path = path.strip('/')
        # Replace / with _ for flat structure
        safe_path = path.replace('/', '_')
        return self.base_path / f"{safe_path}.json"
    
    def _load_cache(self):
        """Load all JSON files into memory cache"""
        try:
            for json_file in self.base_path.rglob("*.json"):
                rel_path = str(json_file.relative_to(self.base_path)).replace('.json', '').replace('_', '/')
                try:
                    with open(json_file, 'r', encoding='utf-8') as f:
                        self._cache[rel_path] = json.load(f)
                except Exception as e:
                    print(f"Warning: Could not load {json_file}: {e}")
        except Exception as e:
            print(f"Warning: Error loading cache: {e}")
    
    def get(self, path: str, default: Any = None) -> Any:
        """Get value from database"""
        with self._lock:
            path = path.strip('/')
            
            # Check cache first
            if path in self._cache:
                return self._cache[path]
            
            # Try to load from file
            file_path = self._get_file_path(path)
            if file_path.exists():
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        data = json.load(f)
                        self._cache[path] = data
                        return data
                except Exception as e:
                    print(f"Error reading {file_path}: {e}")
            
            return default
    
    def set(self, path: str, value: Any) -> bool:
        """Set value in database"""
        with self._lock:
            try:
                path = path.strip('/')
                
                # Update cache
                self._cache[path] = value
                
                # Save to file
                file_path = self._get_file_path(path)
                file_path.parent.mkdir(parents=True, exist_ok=True)
                
                with open(file_path, 'w', encoding='utf-8') as f:
                    json.dump(value, f, indent=2, ensure_ascii=False)
                
                return True
            except Exception as e:
                print(f"Error writing to {path}: {e}")
                return False
    
    def delete(self, path: str) -> bool:
        """Delete value from database"""
        with self._lock:
            try:
                path = path.strip('/')
                
                # Remove from cache
                if path in self._cache:
                    del self._cache[path]
                
                # Delete file
                file_path = self._get_file_path(path)
                if file_path.exists():
                    file_path.unlink()
                
                return True
            except Exception as e:
                print(f"Error deleting {path}: {e}")
                return False
    
    def child(self, path: str) -> 'LocalDatabase':
        """Create a child reference (for compatibility)"""
        return LocalDatabase(str(self.base_path / path.strip('/')))
    
    def update(self, data: Dict[str, Any]) -> bool:
        """Update multiple values"""
        try:
            for key, value in data.items():
                self.set(key, value)
            return True
        except Exception as e:
            print(f"Error updating data: {e}")
            return False

# Global database instance
_db_instance = None
_db_lock = threading.Lock()

def get_database() -> LocalDatabase:
    """Get global database instance"""
    global _db_instance
    with _db_lock:
        if _db_instance is None:
            _db_instance = LocalDatabase()
        return _db_instance

def init_database(base_path: str = "database") -> LocalDatabase:
    """Initialize database with custom path"""
    global _db_instance
    with _db_lock:
        _db_instance = LocalDatabase(base_path)
        return _db_instance

# Compatibility functions for existing Firebase code
class DatabaseReference:
    """Compatibility wrapper for Firebase database references"""
    
    def __init__(self, path: str = ""):
        self.db = get_database()
        self.path = path
    
    def child(self, path: str):
        """Create child reference"""
        new_path = f"{self.path}/{path}".strip('/')
        return DatabaseReference(new_path)
    
    def get(self):
        """Get data"""
        return self.db.get(self.path, {})
    
    def set(self, value):
        """Set data"""
        return self.db.set(self.path, value)
    
    def update(self, data):
        """Update data"""
        if isinstance(data, dict):
            current = self.get() or {}
            if isinstance(current, dict):
                current.update(data)
                return self.db.set(self.path, current)
        return self.db.set(self.path, data)
    
    def delete(self):
        """Delete data"""
        return self.db.delete(self.path)

def get_ref(path: str = "") -> DatabaseReference:
    """Get database reference (Firebase compatibility)"""
    return DatabaseReference(path)

# Initialize on import
init_database()
