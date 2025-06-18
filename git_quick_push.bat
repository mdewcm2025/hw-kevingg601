@echo off
REM git_quick_push.bat
REM 用法： git_quick_push "你的 commit 訊息"
REM 如果沒有傳入參數，腳本會互動式詢問 commit 訊息。

if "%~1"=="" (
    set /p msg=請輸入 commit 訊息: 
) else (
    set msg=%*
)

git add .
git commit -m "%msg%"
git push