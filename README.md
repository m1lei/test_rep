Уровни автоматизации
L1: Статический анализ (Pylint, ESLint) — проверка без запуска.

L2: Динамический анализ (Pytest, JUnit) — выполнение кода и проверка логики.

L3: Quality Gates — автоматические «ворота», которые блокируют мерж при низких метриках.

L4: Мониторинг (Sentry, Prometheus) — контроль качества на живом проекте.

3. Практическая реализация (CI/CD)
В данном проекте настроен пайплайн в GitHub Actions, который включает:

Линтер: Проверка кода на чистоту.

Безопасность: Поиск уязвимостей через bandit.

Тестирование: Запуск Unit-тестов.

Quality Gate: Проверка покрытия кода (минимум 70%).

YAML
# Пример Quality Gate в workflow
- name: Run tests with coverage
  run: pytest --cov=src --cov-fail-under=70

<img width="1075" height="506" alt="Снимок экрана 2026-04-13 в 09 24 44" src="https://github.com/user-attachments/assets/5bc50420-5151-426d-b756-39aae32c5633" />


<img width="1303" height="1092" alt="mYojs" src="https://github.com/user-attachments/assets/f9786ba2-71e5-4b6a-bae9-65fc42535a10" />
