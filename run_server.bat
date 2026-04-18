@echo off
echo ==========================================
echo   Starting financereport Full System...
echo ==========================================

:: 1. Start UI (Python Server)
echo [1/2] Launching UI at http://localhost:8000
start "financereport-UI" python -m http.server 8000

:: 2. Start Backend (Node Server)
echo [2/2] Launching Backend at http://localhost:3000
cd backend
start "financereport-Backend" npm start

echo.
echo [DONE] Both systems are launching in separate windows.
echo Ensure Redis is running on localhost:6379!
echo.
pause
