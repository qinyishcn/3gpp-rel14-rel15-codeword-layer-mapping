# 3GPP Rel-14 / Rel-15 阶段 codeword-to-layer mapping 仿真溯源

**已核对 27 次 RAN1 regular/bis/NR Ad-hoc 会议的 Final Minutes 和 TDoc List；筛选 206 个候选编号，保存 201 份有效提案 ZIP，形成 93 条仿真/适用性证据记录，涉及 77 份文档（含修订与重复结果）和 14 个公司/机构署名组。** 数据截止本次历史检索：2026-10-22。

这些结果没有形成“多 CW / 灵活映射统一提高 X%”的共同 observation。各公司的信道、CSI、接收机、rank、负载和分母不同，结果既有正增益，也有单 CW 更好。最终 Rel-15 选择了有限、固定的 CW-layer mapping 和低处理时延的资源映射。

## 阅读入口

- [Excel 可筛选表](outputs/cw-layer-r14-r15-20261022/codeword-layer-mapping.xlsx)：公司概览、93条证据、正式会议结论、覆盖和源文档。
- [中文研究报告](docs/report.md)：方案、基线、增益、相反结果及最终 observation。
- [逐条仿真全表与原文摘录](docs/simulation-evidence.md) / [CSV](data/simulation-evidence.csv) / [JSON](data/evidence.json)。
- [会议决策链与 observation](docs/meeting-observations.md)。
- [27次会议覆盖及缺口](docs/coverage.md) / [206个候选源目录](data/source-catalog.csv)。
- [原始源文档](sources/) / [SHA-256 清单](data/source-manifest.json)。官方 URL 保存在每条记录中。

## 哪些公司/机构提供了仿真

下面是便于导航的代表结果，均为**提案作者报告**，不是跨公司可直接比较的排行榜。完整条件和基线见证据表。

| 公司/机构署名组 | 仿真 | 代表方案与基线 | 代表结果 | source |
|---|---|---|---|---|
| AT&T | LLS、SLS | 2CW 动态层分组 vs 固定分组 | rank4 SE约+12%；rank8约+18%@20dB；SLS sector约+11% | [R1-1702262](sources/TSGR1_88/Docs/R1-1702262.zip)、[R1-1707737](sources/TSGR1_89/Docs/R1-1707737.zip) |
| Huawei / HiSilicon | SLS、LLS | rank4双CW vs 单CW；高速LTF vs LFT | SLS mean +15.04～17.47%；高速LTF约1.6～4.5dB | [R1-1705073](sources/TSGR1_88b/Docs/R1-1705073.zip)、[R1-1712228](sources/TSGR1_90/Docs/R1-1712228.zip) |
| ZTE / ZTE Microelectronics / Sanechips | SLS、LLS | 双CW vs 单CW；layer-set CBG vs 全层LFT | UMi SU mean +3.72～13.33%；layer-set edge +11.05% | [R1-1701790](sources/TSGR1_88/Docs/R1-1701790.zip)、[R1-1712284](sources/TSGR1_90/Docs/R1-1712284.zip) |
| Intel | SLS、LLS | 单CW vs 双CW；频域交织 | rank≤2单CW mean +4～7%；rank3/4近同；频交织0.3～0.84dB | [R1-1702187](sources/TSGR1_88/Docs/R1-1702187.zip)、[R1-1712536](sources/TSGR1_90/Docs/R1-1712536.zip) |
| Ericsson | SLS | rank3/4双CW vs 单CW | 双CW normalized UPT -2～+4%，作者判断相近 | [R1-1705883](sources/TSGR1_88b/Docs/R1-1705883.zip) |
| Samsung | SLS、LLS | 最多2CW vs 1CW；CW shifting | #88双CW mean为单CW的94.9～98.4%；单CW略好 | [R1-1702916](sources/TSGR1_88/Docs/R1-1702916.zip)、[R1-1705333](sources/TSGR1_88b/Docs/R1-1705333.zip) |
| Qualcomm | LLS；另有CDF推估 | 单CW分层QAM；频域inter-CB交织 | 特定mmW约1.5/7～8dB；LDPC交织0.1～>5dB | [R1-1702596](sources/TSGR1_88/Docs/R1-1702596.zip)、[R1-1708579](sources/TSGR1_89/Docs/R1-1708579.zip) |
| Nokia / Alcatel-Lucent Shanghai Bell | SLS | NCJT/CW组合；相干多panel CW数量 | NCJT部分mean改善，edge不一致；30GHz单CW略好 | [R1-1703150](sources/TSGR1_88/Docs/R1-1703150.zip)、[R1-1705952](sources/TSGR1_88b/Docs/R1-1705952.zip) |
| Xinwei | LLS | CW数量/接收机；FLT vs LFT | 1CW SSD可优于2CW MMSE-SIC；未给统一dB | [R1-1702022](sources/TSGR1_88/Docs/R1-1702022.zip)、[R1-1704661](sources/TSGR1_88b/Docs/R1-1704661.zip) |
| Lenovo / Motorola Mobility | LLS | 联合时频交织 vs 仅频交织 | AWGN约0.9～2.1dB；CDL-A约0.31～3.1dB@CBGER10% | [R1-1710594](sources/NR_AH_1706/Docs/R1-1710594.zip)、[R1-1712670](sources/TSGR1_90/Docs/R1-1712670.zip) |
| MediaTek | LLS | layer-group CBG vs 全层LFT；DFT-s hopping | CLI下同SE可差数dB；特定hopping约1～2dB | [R1-1710815](sources/NR_AH_1706/Docs/R1-1710815.zip)、[R1-1718335](sources/TSGR1_90b/Docs/R1-1718335.zip) |
| NTT DOCOMO | LLS | DFT-s intra-slot hopping Option3 vs Option1 | 多CB约1.5～2dB@BLER10%；单CB相近 | [R1-1718187](sources/TSGR1_90b/Docs/R1-1718187.zip) |
| vivo | LLS | 时频交织 vs 无/仅频交织 | 图示BLER改善，正文未给统一数字 | [R1-1712829](sources/TSGR1_90/Docs/R1-1712829.zip) |
| ETRI | LLS | 高速LTF、multi-symbol交织 vs LFT | 500km/h图示BLER改善，正文未给统一dB | [R1-1710611](sources/NR_AH_1706/Docs/R1-1710611.zip)、[R1-1713808](sources/TSGR1_90/Docs/R1-1713808.zip) |

## 最终形成了什么

1. **CW数量及空间层映射**：NR DL 1–4层为1CW，5–8层为2CW；高秩分割为2+3、3+3、3+4、4+4。NR UL最多4层为1CW。见 [TS 38.211 V15.2.0 (2018-06), §6.3.1.3、§7.3.1.3/Table7.3.1.3-1, Normative](sources/specs/38211-f20.zip)。
2. **额外灵活对应**：#90bis明确Rel-15 >4层不增加CW-layer correspondence；2/3/4层增加2CW在2017年12月完成范围内没有共识。见 [#90bis Final Minutes §7.2.1.1, Meeting outcome](sources/TSGR1_90b/Report/Final_Minutes_report_RAN1%2390b_v100.zip)。
3. **映射顺序和交织**：#90选择DL与CP-OFDM UL的L→F→T，不支持本议题中的额外频率/时间交织。见 [#90 Final Minutes §6.1.2.1.1, Meeting outcome](sources/TSGR1_90/Report/Final_Minutes_report_RAN1%2390_v100.zip)。这不表示NR没有编码内交织或VRB-to-PRB interleaving。
4. **DFT-s-OFDM intra-slot hopping**：#91最终确认先子载波、再sub-slot内symbol、最后不同PRB的sub-slot，并扩展到多CB。见 [#91 Final Minutes §7.2.1.1, Meeting outcome](sources/TSGR1_91/Report/Final_Minutes_report_RAN1%2391_v100.zip)。

## 范围与证据边界

“Rel-14阶段”按会议时期检索；2016年启动的NR study不等于LTE Rel-14已引入同一功能。LTE既有条文另核对 [TS 36.211 V14.3.0, §6.3.3.2/Table6.3.3.2-1, Normative](sources/specs/36211-e30.zip)。该ZIP分4个Word文件，相关正文在`s06-s08`，不是cover。

未下载全部54,418篇TDoc全文；这是从正式会议报告、官方标题、专题提案及引用链得到的可审计检索集。93条记录不是93个独立实验。4个无文件编号（1个已被修订、3个withdrawn）和1个损坏ZIP列在[覆盖说明](docs/coverage.md)。没有用标题、`agreed/noted`状态、共同署名或公司沉默推断详细立场。

## 复核与下载

```powershell
python scripts/verify_sources.py
# 缺少原始文件时：优先HTTPS，失败后匿名被动FTP；已有正确文件跳过
python scripts/download_sources.py
```

原始文档版权归3GPP及原署名机构；本仓库保留来源和哈希，不对第三方原文附加开源许可。分析、抽取文本和表格用于研究溯源，原始Word中的公式/表格/图优先于抽取文本。
