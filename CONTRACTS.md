# Support contracts — v2.2.0 / schema 3

Target: Victoria 3 1.13.11 (`supported_version=1.13.*`). Baseline: NVGM 2.1.1.

## Implemented

Recipient-country records hold the resource amount and original issuer. Donor indices additionally store the recipient generation. Donor costs are rebuilt as one aggregate modifier per resource; old slot modifiers and mirrors are regenerated. Each kind has a separate monotonically increasing generation. Existing complete v2.1.1 links import lazily on use or the monthly pulse. Import never infers a donor from a matching amount.

Subsidy membership captures the recipient country and generation on each building. A batch rotates the generation once, retains other valid managed targets, then adds only previously unsubsidized targets. Only NVGM-owned toggles are disabled on close. General-aid conditions remain per building so mixed funded and coerced legacy subsidies keep their existing behavior. Losing general aid removes only aid-dependent targets. This is an explicit compatibility refinement of the draft’s single country-wide aid flag.

Independent/subject hooks run the existing unified cleanup immediately and the following day. Active subsidy contracts also have one scheduled daily watchdog per recipient for relation and lease checks. The watchdog never renews the lease. Monthly validated cleanup renews the 45-day token; missed renewal pauses subsidies at the next watchdog tick. Resource modifiers expire after 45 days. A stopped/expired resource contract is closed and must be started again explicitly. The explicit resume operation currently applies to paused subsidy contracts.

Membership counts detect lost, moved or manually disabled targets. Ownership checks on the new owner remove foreign stale membership during its cleanup. A whole-world repair path is retained. These scripts do not promise zero-tick cleanup for an ownership change without a confirmed engine hook.

The subsidy stop/resume controls are added to the existing management panel. Repair and stop-all decisions remain available. Stop is authorized for the recipient or recorded sponsor without requiring a current subject relation. Unknown future schema blocks contract mutations. The generation ceiling is 1,000,000; it never wraps. The final generation is usable, but another batch cannot be opened.

## Not implemented

Exact full-cost subsidy reimbursement, financial ledgers and unpaid claims are not active in this release. The capability trigger is hard-disabled; its button explains why. No guessed expense API, GDP-based estimate, treasury transfer, automatic debt or write-off is introduced. Ordinary existing money-transfer actions retain their prior behavior.

Explicit adoption of already subsidized buildings into a financial contract is also deferred. Existing company and industry calls keep their original previously-unsubsidized-only rule.

## Migration and compatibility

Migration commits `nvgm_contract_schema=3` last. Existing subsidies without an NVGM marker remain untouched. Old assistance markers become tracking/general-aid conditions, never financial consent. Generation counters survive closure. Use a copy of a pre-upgrade save for testing and retain it to roll back: a migrated save is not promised to work in 2.1.1.

Original 1.7.8 and unavailable 2.0.0 saves have no direct migration guarantee. Native load validation and model execution are separate from real saved-game, economy and multiplayer tests.

## Overrides

No new Vanilla overrides or replace_path. Existing raise_payments/decrease_payments, diplomatic_overview.gui/ingame_hud.gui and city type overrides remain. The diplomatic GUI is changed within its existing override. Mods that change the same GUI, subsidy toggles or NVGM variables can conflict.
