param(
    [string]$LedgerPath  = "attestation/ledger.log",
    [string]$SigPath     = "attestation/ledger.sshsig",
    [string]$PubKeyPath  = "attestation/keys/pub_ed25519.openssh"
)

Write-Host "🔍 HUMEAN · Vérification du ledger signé" -ForegroundColor Cyan
Write-Host "  Ledger     : $LedgerPath"
Write-Host "  Signature  : $SigPath"
Write-Host "  Clé publique : $PubKeyPath"
Write-Host ""

$err = $false

if (!(Test-Path $LedgerPath)) {
    Write-Host "❌ Ledger introuvable : $LedgerPath" -ForegroundColor Red
    $err = $true
}
if (!(Test-Path $SigPath)) {
    Write-Host "❌ Signature introuvable : $SigPath" -ForegroundColor Red
    $err = $true
}
if (!(Test-Path $PubKeyPath)) {
    Write-Host "❌ Clé publique introuvable : $PubKeyPath" -ForegroundColor Red
    $err = $true
}

if ($err) {
    Write-Host "⛔ Vérification annulée (fichier(s) manquant(s))." -ForegroundColor Red
    exit 2
}

# on est sûr que les 3 existent → on vérifie
try {
    Get-Content $LedgerPath | ssh-keygen -Y verify -f $PubKeyPath -I "humean" -n file -s $SigPath
    if ($LASTEXITCODE -eq 0) {
        Write-Host "✅ Signature VALIDE pour le ledger." -ForegroundColor Green
        exit 0
    } else {
        Write-Host "❌ Signature INVALIDE (ssh-keygen a renvoyé $LASTEXITCODE)." -ForegroundColor Red
        exit 1
    }
}
catch {
    Write-Host "❌ Erreur pendant la vérif ssh-keygen : $_" -ForegroundColor Red
    exit 255
}
