# Claims

Each YAML file is one record. Filename stem **must** equal `id`.

None of these are `reviewed`. That is intentional.

| id | status | confidence | title |
|----|--------|------------|-------|
| [atm-swipe-share](atm-swipe-share.yaml) | proposed | low | Share of ATM swipes that rely on COBOL |
| [average-programmer-age](average-programmer-age.yaml) | contested | low | Average age of COBOL programmers |
| [banking-systems-share](banking-systems-share.yaml) | proposed | low | Share of banking systems built on COBOL |
| [cics-link-lower-logical-level](cics-link-lower-logical-level.yaml) | proposed | medium | EXEC CICS LINK passes control to a program at the next lower logical level |
| [cics-xctl-same-logical-level](cics-xctl-same-logical-level.yaml) | proposed | medium | EXEC CICS XCTL transfers control at the same logical level and releases the caller |
| [copy-nested-one-replacing](copy-nested-one-replacing.yaml) | proposed | high | A nested COPY chain may contain only one COPY REPLACING |
| [copy-replaces-statement-with-library-text](copy-replaces-statement-with-library-text.yaml) | proposed | high | COPY replaces itself, from COPY through the period, with library text |
| [corpus-opencbs-43-programs](corpus-opencbs-43-programs.yaml) | proposed | medium | OpenCBS is a 43-program COBOL defect suite from public forums |
| [corresponding-same-name-elementary](corresponding-same-name-elementary.yaml) | proposed | high | CORRESPONDING operates on same-named elementary items in two groups |
| [daily-commerce-volume](daily-commerce-volume.yaml) | proposed | low | Daily commerce processed through COBOL systems |
| [dynam-call-literal-runtime-load](dynam-call-literal-runtime-load.yaml) | proposed | high | DYNAM loads CALL literal targets at run time; default is NODYNAM |
| [enterprise-cobol-qsam-vsam-unix](enterprise-cobol-qsam-vsam-unix.yaml) | proposed | high | Enterprise COBOL z/OS I/O is QSAM, VSAM, or the z/OS UNIX file system |
| [evaluate-shorthand-nested-if](evaluate-shorthand-nested-if.yaml) | proposed | high | EVALUATE is a shorthand for a series of nested IF statements |
| [gnucobol-goback-main-stop-run-sub-exit](gnucobol-goback-main-stop-run-sub-exit.yaml) | proposed | medium | In GnuCOBOL, GOBACK is STOP RUN in a main program and EXIT PROGRAM in a subprogram |
| [gnucobol-std-ibm-compatible](gnucobol-std-ibm-compatible.yaml) | proposed | medium | GnuCOBOL -std=ibm selects an IBM-compatible dialect |
| [goback-stop-run-exit-program](goback-stop-run-exit-program.yaml) | proposed | high | EXIT PROGRAM, STOP RUN, and GOBACK terminate differently |
| [history-codasyl-1959](history-codasyl-1959.yaml) | proposed | high | COBOL began as a CODASYL Short Range Committee specification in 1959-1960 |
| [ims-cobol-cbltdli](ims-cobol-cbltdli.yaml) | proposed | medium | IMS COBOL programs issue DL/I through CALL CBLTDLI |
| [in-person-transactions-share](in-person-transactions-share.yaml) | proposed | low | Share of in-person transactions that use COBOL |
| [initialize-equivalent-to-moves](initialize-equivalent-to-moves.yaml) | proposed | high | INITIALIZE is functionally equivalent to one or more MOVE statements |
| [jcl-dd-describes-dataset](jcl-dd-describes-dataset.yaml) | proposed | high | A JCL DD statement identifies and describes a data set |
| [jcl-exec-identifies-program](jcl-exec-identifies-program.yaml) | proposed | high | A JCL EXEC statement starts a step and names the program or procedure |
| [json-generate-from-cobol-data](json-generate-from-cobol-data.yaml) | proposed | high | JSON GENERATE produces JSON text from COBOL data items |
| [knowledge-not-syntax](knowledge-not-syntax.yaml) | proposed | medium | The scarce asset is institutional knowledge, not COBOL syntax |
| [level-88-condition-name-value](level-88-condition-name-value.yaml) | proposed | high | Level-88 entries name values of a preceding conditional variable |
| [loc-in-production](loc-in-production.yaml) | contested | low | Lines of COBOL in production |
| [lp-option-amode-31-or-64](lp-option-amode-31-or-64.yaml) | proposed | high | LP(32) generates AMODE 31; LP(64) generates AMODE 64 |
| [national-usage-utf16-two-bytes](national-usage-utf16-two-bytes.yaml) | proposed | high | USAGE NATIONAL stores UTF-16; each PICTURE position takes 2 bytes |
| [nested-programs-contained](nested-programs-contained.yaml) | proposed | high | Nested programs are COBOL programs contained in other COBOL programs |
| [numproc-nopfd-nonpreferred-signs](numproc-nopfd-nonpreferred-signs.yaml) | proposed | high | NUMPROC(NOPFD) accepts nonpreferred decimal signs; default is NOPFD |
| [perform-inline-omits-procedure-name](perform-inline-omits-procedure-name.yaml) | proposed | high | Inline PERFORM omits procedure-name-1 and requires END-PERFORM |
| [picture-character-string-max-50](picture-character-string-max-50.yaml) | proposed | high | A PICTURE character-string is at most 50 characters |
| [picture-clause-elementary-required](picture-clause-elementary-required.yaml) | proposed | high | PICTURE is required on elementary items except a short exclusion list |
| [picture-numeric-symbols-9-p-s-v](picture-numeric-symbols-9-p-s-v.yaml) | proposed | high | Numeric PICTURE strings use only 9, P, S, and V |
| [redefines-same-computer-storage](redefines-same-computer-storage.yaml) | proposed | high | REDEFINES describes the same storage with a different layout |
| [rent-reentrant-object-default](rent-reentrant-object-default.yaml) | proposed | high | RENT (the default) generates a reentrant object program |
| [retirement-rate](retirement-rate.yaml) | contested | low | COBOL practitioner annual retirement rate |
| [ssrange-runtime-range-check](ssrange-runtime-range-check.yaml) | proposed | high | SSRANGE generates runtime checks of subscripts and reference modification |
| [trunc-bin-treats-binary-as-comp5](trunc-bin-treats-binary-as-comp5.yaml) | proposed | high | TRUNC(BIN) treats BINARY, COMP, and COMP-4 as COMP-5 |
| [trunc-std-picture-digits](trunc-std-picture-digits.yaml) | proposed | high | TRUNC(STD) truncates BINARY receivers to PICTURE digit count |
| [university-teaching](university-teaching.yaml) | proposed | medium | Universities largely stopped teaching COBOL |
| [usage-binary-comp-comp4-synonyms](usage-binary-comp-comp4-synonyms.yaml) | proposed | high | BINARY, COMP, and COMP-4 are synonyms occupying 2, 4, or 8 bytes |
| [usage-clause-not-level-66-or-88](usage-clause-not-level-66-or-88.yaml) | proposed | high | USAGE may be specified at any level except 66 or 88 |
| [usage-comp3-packed-decimal-storage](usage-comp3-packed-decimal-storage.yaml) | proposed | high | COMP-3 is PACKED-DECIMAL; two digits per byte except the sign nibble |
| [usage-comp5-native-binary-range](usage-comp5-native-binary-range.yaml) | proposed | high | COMP-5 holds the full native binary range, truncating at field size |
| [usage-pointer-4-or-8-bytes](usage-pointer-4-or-8-bytes.yaml) | proposed | high | USAGE POINTER is 4 bytes under LP(32) and 8 bytes under LP(64) |
| [xml-parse-to-processing-procedure](xml-parse-to-processing-procedure.yaml) | proposed | high | XML PARSE passes each piece of an XML document to a processing procedure |
