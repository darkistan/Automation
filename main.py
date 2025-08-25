#!/usr/bin/env python3
"""
Основний файл проекту автоматизації.
Містить базову структуру та конфігурацію.
"""

import os
import sys
from pathlib import Path


def setup_environment():
    """Налаштовує середовище для роботи проекту."""
    # Додаємо поточну директорію до Python path
    project_root = Path(__file__).parent
    sys.path.insert(0, str(project_root))
    
    # Завантажуємо змінні середовища
    env_file = project_root / ".env"
    if env_file.exists():
        from dotenv import load_dotenv
        load_dotenv(env_file)
    
    print(f"Проект ініціалізовано: {project_root}")


def main():
    """Головна функція проекту."""
    print("🚀 Запуск проекту автоматизації...")
    
    try:
        setup_environment()
        print("✅ Середовище налаштовано успішно")
        
        # Тут буде основна логіка проекту
        print("📋 Готово до роботи!")
        
    except Exception as e:
        print(f"❌ Помилка: {e}")
        return 1
    
    return 0


if __name__ == "__main__":
    sys.exit(main()) 