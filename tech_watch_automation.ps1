# Tech Watch Automation Script
# Usage: .\tech_watch_automation.ps1

Write-Host "================================" -ForegroundColor Cyan
Write-Host "  LLM Council - Tech Watch" -ForegroundColor Cyan
Write-Host "  Automation Script" -ForegroundColor Cyan
Write-Host "================================" -ForegroundColor Cyan
Write-Host ""

# Configuration
$env:PYTHONIOENCODING = "utf-8"
$projectRoot = "C:\Users\Utilisateur\Desktop\projects\LLM Council"
$outputDir = "tech-watch\$(Get-Date -Format 'yyyy-MM')"

# Create output directory
New-Item -ItemType Directory -Force -Path $outputDir | Out-Null
Write-Host "[OK] Output directory: $outputDir" -ForegroundColor Green
Write-Host ""

# Define research topics (customize these!)
$topics = @(
    @{
        Name = "kubernetes-security"
        Question = "Latest Kubernetes security features and best practices in 2025: CVEs, security tools, mTLS, RBAC improvements, verified sources"
        Models = "ollama:deepseek-coder:6.7b", "ollama:llama3.1:8b", "ollama:mistral:7b", "gemini"
        Rounds = 4
    },
    @{
        Name = "ai-deployment"
        Question = "LLM deployment strategies in 2025: cloud vs local, quantization techniques, cost analysis, performance benchmarks with references"
        Models = "ollama:llama3.1:8b", "ollama:mistral:7b", "gemini"
        Rounds = 4
    },
    @{
        Name = "cloud-trends"
        Question = "Cloud-native trends Q1 2025: service mesh, eBPF, GitOps, cost optimization, industry adoption with statistics"
        Models = "ollama:llama3.1:8b", "ollama:mistral:7b", "gemini"
        Rounds = 3
    }
)

Write-Host "Topics to research: $($topics.Count)" -ForegroundColor Yellow
Write-Host ""

# Run research for each topic
$successCount = 0
$failCount = 0

foreach ($topic in $topics) {
    Write-Host "-----------------------------------" -ForegroundColor Cyan
    Write-Host "Researching: $($topic.Name)" -ForegroundColor Yellow
    Write-Host "-----------------------------------" -ForegroundColor Cyan
    
    # Build models argument
    $modelsArg = $topic.Models -join " "
    
    # Run debate
    try {
        Set-Location $projectRoot
        
        $command = "python main.py `"$($topic.Question)`" --models $modelsArg --rounds $($topic.Rounds)"
        Write-Host "Command: $command" -ForegroundColor DarkGray
        Write-Host ""
        
        Invoke-Expression $command
        
        if ($LASTEXITCODE -eq 0) {
            $successCount++
            Write-Host "[SUCCESS] $($topic.Name) completed!" -ForegroundColor Green
            
            # Move generated files
            $timestamp = Get-Date -Format "yyyyMMdd"
            Move-Item -Path "debate_*.json" -Destination "$outputDir\" -ErrorAction SilentlyContinue
            Move-Item -Path "article_*.md" -Destination "$outputDir\" -ErrorAction SilentlyContinue
        } else {
            $failCount++
            Write-Host "[ERROR] $($topic.Name) failed!" -ForegroundColor Red
        }
    }
    catch {
        $failCount++
        Write-Host "[ERROR] Exception: $_" -ForegroundColor Red
    }
    
    Write-Host ""
    
    # Small delay between topics
    if ($topic -ne $topics[-1]) {
        Write-Host "Waiting 5 seconds before next topic..." -ForegroundColor DarkGray
        Start-Sleep -Seconds 5
    }
}

# Summary
Write-Host "================================" -ForegroundColor Cyan
Write-Host "  TECH WATCH COMPLETE!" -ForegroundColor Cyan
Write-Host "================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "[OK] Successful: $successCount" -ForegroundColor Green
Write-Host "[X] Failed: $failCount" -ForegroundColor $(if ($failCount -gt 0) { "Red" } else { "Green" })
Write-Host ""
Write-Host "Results saved to: $outputDir" -ForegroundColor Yellow
Write-Host ""

# List generated files
$jsonFiles = Get-ChildItem -Path $outputDir -Filter "*.json" | Measure-Object
$mdFiles = Get-ChildItem -Path $outputDir -Filter "*.md" | Measure-Object

Write-Host "Generated files:" -ForegroundColor Yellow
Write-Host "  - JSON: $($jsonFiles.Count)" -ForegroundColor White
Write-Host "  - Markdown: $($mdFiles.Count)" -ForegroundColor White
Write-Host ""

Write-Host "================================" -ForegroundColor Cyan
Write-Host ""

