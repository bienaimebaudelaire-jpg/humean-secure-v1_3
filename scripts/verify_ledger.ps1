<#
    verify-ledger.ps1
    Vérifie l’intégrité du journal HUMEAN (ledger_signed.jsonl)
#>

Write-Host "🔍 Vérification du ledger HUMEAN..." -ForegroundColor Cyan

$repoRoot = Get-Location
$ledgerPath = Join-Path $repoRoot "log\ledger_signed.jsonl"

if (!(Test-Path $ledgerPath)) {
    Write-Host "❌ Ledger signé introuvable à l'emplacement : $ledgerPath" -ForegroundColor Red
    exit 1
}

try {
    $lines = Get-Content $ledgerPath -Raw
    if ($lines.Length -lt 10) {
        Write-Host "⚠️ Ledger trouvé mais semble vide ou corrompu." -ForegroundColor Yellow
        exit 2
    }

    $hash = (Get-FileHash -Algorithm SHA256 $ledgerPath).Hash
    Write-Host "✅ Ledger détecté et lisible." -ForegroundColor Green
    Write-Host "🔹 SHA256 : $hash"
    exit 0
}
catch {
    Write-Host "❌ Erreur de lecture du ledger : $_" -ForegroundColor Red
    exit 255
}
