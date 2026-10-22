# 会议覆盖与检索边界

检查27次会议的Final Minutes和官方TDoc List，共54,418条TDoc记录。按标题宽松筛查CW数量/映射、layer mapping、interleaving、CB mapping，再沿报告和参考文献回查。候选不是全部被完整深读的相关标准体系。未对54,418篇全文下载。

| 会议 | 官方TDoc数 | 标题候选 | 有效下载 | 纳入仿真文档 | 报告章节 |
|---|---:|---:|---:|---:|---|
| NR_AH_1701 | 1549 | 15 | 15 | 7 | 5.1.2.1 Multi-antenna scheme 26 |
| NR_AH_1706 | 2138 | 20 | 19 | 11 | 5.1.2.1 Multi-antenna scheme 32; 5.1.2.1.1 Codeword mapping 32 |
| NR_AH_1709 | 1584 | 17 | 16 | 6 | 6.2.1 Multi-antenna scheme 29; 6.2.1.1 Remaining details on codeword mapping 29 |
| NR_AH_1801 | 1297 | 6 | 6 | 0 | 7.2.1 Multi-antenna scheme 38; 7.2.1.1 Codeword mapping 38 |
| TSGR1_80 | 966 | 0 | 0 | 0 |  |
| TSGR1_80b | 1225 | 0 | 0 | 0 |  |
| TSGR1_81 | 1266 | 0 | 0 | 0 |  |
| TSGR1_82 | 1321 | 0 | 0 | 0 |  |
| TSGR1_82b | 1376 | 0 | 0 | 0 |  |
| TSGR1_83 | 1527 | 0 | 0 | 0 |  |
| TSGR1_84 | 1333 | 0 | 0 | 0 |  |
| TSGR1_84b | 1855 | 0 | 0 | 0 |  |
| TSGR1_85 | 2094 | 0 | 0 | 0 | 7.1.6 Multi-antenna scheme for new radio interface 113 |
| TSGR1_86 | 2506 | 0 | 0 | 0 | 8.1.5 Multi-antenna scheme for new radio interface 99 |
| TSGR1_86b | 2514 | 1 | 1 | 0 | 8.1.4 Multi-antenna scheme for new radio interface 91; 8.1.4.2 Multi-antenna scheme 96 |
| TSGR1_87 | 2741 | 3 | 3 | 1 | 7.1.3.1 Multi-antenna scheme 94 |
| TSGR1_88 | 2614 | 21 | 21 | 12 | 8.1.2.1 Multi-antenna scheme 73; 8.1.2.1.1 Codeword mapping 74 |
| TSGR1_88b | 2688 | 20 | 20 | 10 | 8.1.2.1 Multi-antenna scheme 74; 8.1.2.1.1 Codeword mapping 74 |
| TSGR1_89 | 3005 | 22 | 22 | 8 | 7.1.2.1 Multi-antenna scheme 83; 7.1.2.1.1 Codeword mapping 83 |
| TSGR1_90 | 3309 | 25 | 24 | 11 | 6.1.2.1 Multi-antenna scheme 81; 6.1.2.1.1 Remaining details on codeword mapping 81 |
| TSGR1_90b | 2315 | 15 | 14 | 7 | 7.2.1 Multi-antenna scheme 80; 7.2.1.1 Remaining details on codeword mapping 80 |
| TSGR1_91 | 2436 | 15 | 15 | 4 | 7.2.1 Remaining details on Multi-antenna scheme 91; 7.2.1.1 Remaining details on codeword mapping 91 |
| TSGR1_92 | 2257 | 6 | 6 | 0 | 7.1.2.1 Multi-antenna scheme 75; 7.1.2.1.1 Codeword mapping 75 |
| TSGR1_92b | 2230 | 10 | 9 | 0 | 7.1.2.1 Multi-antenna scheme 66; 7.1.2.1.1 Codeword mapping 66 |
| TSGR1_93 | 2175 | 7 | 7 | 0 | 7.1.2.1 Multi-antenna scheme 68; 7.1.2.1.1 Codeword mapping 69 |
| TSGR1_94 | 2050 | 3 | 3 | 0 | 7.1.2.1 Maintenance for Multi-antenna scheme 47 |
| TSGR1_94b | 2047 | 0 | 0 | 0 | 7.1.2.1 Maintenance for Multi-antenna scheme 39 |

## 缺口

- NR_AH_1706 R1-1711635 — not_present_in_official_directory；官方目录无文件；TDoc List状态=revised；Revised to=R1-1711935。官方标题：Summary of Open Issues on Layer Mapping。
- NR_AH_1709 R1-1716833 — not_present_in_official_directory；官方目录无文件；TDoc List状态=withdrawn；Revised to=。官方标题：Remaining Issues on CW to layer mapping。
- TSGR1_90 R1-1714935 — not_present_in_official_directory；官方目录无文件；TDoc List状态=withdrawn；Revised to=。官方标题：Codeword mapping in NR。
- TSGR1_90b R1-1718798 — official_archive_invalid_or_truncated；官方ZIP返回25728字节、无ZIP central directory；正式会议记录保留同号讨论。官方标题：Summary of Open Issues on Layer Mapping。
- TSGR1_92b R1-1803737 — not_present_in_official_directory；官方目录无文件；TDoc List状态=withdrawn；Revised to=。官方标题：WF on codeword mapping。

R1-1709356为旧PPT，已保留ZIP并用本地PowerPoint转换抽取；没有把不支持的格式当成无内容。R1-1718798 的HTTPS原始返回25728字节，无ZIP central directory，匿名FTP两次也未通过ZIP完整性验证；不作为有效源文件计数。R1-1711635已由官方List指向R1-1711935，后者已下载。其余3个无文件编号官方List为withdrawn。

2015–2016早期报告无独立CW mapping标题命中，并不证明LTE Rel-14或所有公司不存在相关仿真。本报告能确认的主线是2016#86bis开始的NR CW mapping研究及2017 Rel-15下选；LTE Rel-14的既有mapping另以TS 36.211 V14.3.0作规范背景，不将NR study在R14时段的提案改称LTE R14已采纳功能。

一般MIMO、MUST、CoMP、接收机研究的全部仿真不自动纳入；只有明确比较CW数量、层分组、映射/交织或其适用统计的结果列入。CATT、LG、Sony、Potevio等在若干文档提出方案或引用其他公司结果，不因WF共同署名或TDoc标题就计为独立仿真提供方。