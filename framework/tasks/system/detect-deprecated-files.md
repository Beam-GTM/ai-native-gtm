# Detect and Remove Deprecated Files | System Hygiene Task

**Purpose**: Systematic detection and removal of deprecated files to maintain single source of truth  
**Trigger**: POST-ACTION verification detects duplicate filenames or version conflicts  
**Frequency**: After system modifications, before major consolidations  
**Learning Source**: Learning #073 - Deprecated Files Are Detrimental

## 🔍 DEPRECATED FILE DETECTION PROTOCOL

### Phase 1: Version Analysis Detection
**Objective**: Identify files with version conflicts

```bash
# Scan for files with similar names but different versions
find  -name "*ENHANCED*" -o -name "*-v[0-9]*" -o -name "*_backup*" -o -name "*-old*"

# Check for version headers in similar files
grep -r "version:" framework/ | grep -E "(v[0-9]+\.[0-9]+|[0-9]+\.[0-9]+)"
```

**Detection Criteria**:
- ✅ Files with same base name but version suffixes (-ENHANCED, -v2, -backup)
- ✅ Different version headers in similar content files  
- ✅ Last-modified dates showing clear supersession pattern
- ✅ Content overlap >70% between files

### Phase 2: Reference Analysis
**Objective**: Verify which files are actively referenced

```bash
# Check references in static-base-activation.md
grep -r "CRITICAL-DIRECTIVES" framework/activation/

# Scan orchestrator and agent references
grep -r "CRITICAL-DIRECTIVES" operations/agents/

# Find template references
grep -r "CRITICAL-DIRECTIVES" framework/templates/
```

**Reference Priority**:
1. **CRITICAL**: Static activation references (always-loaded files)
2. **HIGH**: Orchestrator agent references (system core)  
3. **MEDIUM**: Template system references (generation)
4. **LOW**: Documentation references (explanatory)

### Phase 3: Content Comparison
**Objective**: Determine which version contains latest learnings

```bash
# Compare file sizes (larger often = more comprehensive)
ls -la framework/CRITICAL-DIRECTIVES*

# Compare last-modified dates  
stat framework/CRITICAL-DIRECTIVES*

# Count directive numbers (if numbered)
grep -c "DIRECTIVE #" framework/CRITICAL-DIRECTIVES*
```

**Supersession Indicators**:
- ✅ Newer last-modified date
- ✅ Higher version number in file
- ✅ More comprehensive directive count
- ✅ References to recent learnings/sessions

### Phase 4: Safety Verification
**Objective**: Prevent accidental deletion of current systems

**MANDATORY CHECKS**:
1. **Version Header Verification**: Read version metadata from file headers
2. **Date Verification**: Compare last-modified timestamps  
3. **Reference Count**: Count active system references
4. **Content Analysis**: Verify no unique critical content in deprecated version
5. **User Confirmation**: Require explicit approval for deletion

### Phase 5: Systematic Removal
**Objective**: Safe removal with backup preservation

```bash
# Create safety backup before removal
mkdir -p workspace/backups/deprecated-files-$(date +%Y-%m-%d)/
cp [deprecated-file] workspace/backups/deprecated-files-$(date +%Y-%m-%d)/

# Remove deprecated file
rm [deprecated-file]

# Verify removal successful
ls -la [file-location] # Should show only current version remains
```

## 🚨 SAFETY PROTOCOLS

### Pre-Removal Checklist
- [ ] Version comparison completed (newer version confirmed)
- [ ] Reference analysis shows zero active references to deprecated file
- [ ] Content verification confirms no unique critical information
- [ ] Safety backup created in workspace/backups/deprecated-files/
- [ ] User approval obtained for deletion
- [ ] POST-ACTION verification planned to confirm single source of truth

### Emergency Recovery
If wrong file deleted:
1. **STOP** all operations immediately
2. **RESTORE** from workspace/backups/deprecated-files-[date]/
3. **RE-ANALYZE** version comparison with corrected criteria
4. **DOCUMENT** error as learning for mechanism improvement
5. **ENHANCE** safety protocols to prevent recurrence

## 🎯 INTEGRATION POINTS

### POST-ACTION Verification Integration
Add to DIRECTIVE #14 POST-ACTION verification:
- ✅ Did this action create any duplicate files?
- ✅ Are there version conflicts requiring deprecation cleanup?
- ✅ Should detect-deprecated-files task be triggered?

### Systematic Triggers
**Automatic Detection**:
- After system modifications that create versioned files
- Before major consolidation operations  
- During system-sync comprehensive validation
- When POST-ACTION verification detects conflicts

**Manual Execution**:
- User reports confusion between similar files
- System analysis reveals multiple sources of truth
- Before template generation to ensure clean base
- Periodic system hygiene maintenance

## 📊 SUCCESS METRICS

### Detection Effectiveness
- **Files Identified**: Count of deprecated files detected per scan
- **False Positives**: Active files incorrectly flagged (target: 0%)  
- **Reference Accuracy**: Correct identification of unused files
- **Version Conflicts**: Duplicate truth sources identified

### Removal Safety
- **Zero Data Loss**: No unique content accidentally deleted
- **Recovery Success**: 100% restoration capability via backups
- **User Satisfaction**: Reduced confusion from file proliferation
- **System Integrity**: Single source of truth maintained

## 🔄 CONTINUOUS IMPROVEMENT

### Learning Integration
- Capture patterns in deprecated file creation
- Enhance detection algorithms based on findings
- Update safety protocols from near-miss incidents
- Evolve criteria for version supersession detection

### Mechanism Evolution
Version 1.0: Basic version/date comparison with manual verification
Version 2.0: Reference analysis integration with automated safety checks  
Version 3.0: Content analysis AI with predictive deprecation warnings
Version 4.0: Real-time duplicate detection with prevention protocols

---

**CRITICAL SUCCESS FACTOR**: This mechanism must NEVER delete current/active files based on similarity alone. Version verification and reference analysis are MANDATORY safety gates that prevent knowledge destruction through automated cleanup.