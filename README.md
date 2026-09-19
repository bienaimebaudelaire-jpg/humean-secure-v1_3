> ⚠️ **Archivé** — Ce scaffold de gouvernance/attestation est remplacé par [`humean-ecosystem`](https://github.com/bienaimebaudelaire-jpg/humean-ecosystem) (voir `docs/ARCHITECTURE.md`, `docs/DECISIONS.md`, `docs/PRODUCT_BOUNDARIES.md`). Conservé ici pour historique.

---

# HUMEAN - You Mean. We Mean. To Be Human.

HUMEAN = IA x Humanite with verifiable guarantees (charters, policies, attestations).

Local verify:
    cat attestation/ledger.log | ssh-keygen -Y verify -f attestation/keys/pub_ed25519.openssh -I humean -n file -s attestation/ledger.sshsig

License: AGPL-3.0
