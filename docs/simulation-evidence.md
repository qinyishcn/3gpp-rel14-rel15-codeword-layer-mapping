# 仿真证据全表

每条均为 Proposal 中的作者报告结果；均不代表统一3GPP认可增益。字段“限制”注明分母、重复、接收机变化或原文笔误。原ZIP及抽取文本均随库提供。

| ID | 公司/机构 | 会议/TDoc | 类型/议题 | 方案与基线 | 结果 | 关键条件 | 原文定位 | 限制 |
|---|---|---|---|---|---|---|---|---|
| E001 | Qualcomm Incorporated | TSGR1_87 [R1-1612738](../sources/TSGR1_87/Docs/R1-1612738.zip) | LLS / CW数量 | Rank2用1CW；基线：Rank2用2CW，Rank1两者均1CW | CL/OL例子性能接近；正文未给统一百分比 | LTE numerology/2x2；DMRS估计；advanced RX；Turbo；IR最多4重传 | Performance evaluation / Observation 3 / two throughput figures |  |
| E002 | ZTE, ZTE Microelectronics | TSGR1_88 [R1-1701790](../sources/TSGR1_88/Docs/R1-1701790.zip) | SLS / CW数量 | Rank2用2CW、每CW链路自适应/HARQ；基线：Rank2用1CW | Indoor SU：mean UPT +5.52/+8.41/+8.06%；5%-UPT +23.30/+3.07/+17.45% | 3.5GHz/10MHz；2Rx；FTP目标负载20/50/80%；MMSE-IRC | Single-TRP / Table 1 |  |
| E003 | ZTE, ZTE Microelectronics | TSGR1_88 [R1-1701790](../sources/TSGR1_88/Docs/R1-1701790.zip) | SLS / CW数量 | Rank2用2CW；基线：Rank2用1CW | UMi SU：mean +3.72～13.33%；5%-UPT +19.42～55.14%；MU：average SE +2.96%、5%-SE +31.90% | UMi 2GHz/10MHz/2Rx；SU FTP λ2.6/3.5/4.6/5.6，MU full buffer、最多4 MU layers | Single-TRP / Tables 2–3 |  |
| E004 | ZTE, ZTE Microelectronics | TSGR1_88 [R1-1701790](../sources/TSGR1_88/Docs/R1-1701790.zip) | SLS / NC-JT整体方案 | 2TRP NC-JT、每TRP独立CW；基线：单TRP DPS/DPB，基线Rank2已经用2CW | 4Rx/3.5GHz：mean +14.25～34.98%、5% +15.95～28.27%；2Rx/RU≈80%：mean +19.69%(3.5GHz)/+6.60%(30GHz) | Indoor/ideal backhaul；4Rx目标RU5/20/40/70%，2Rx高负载 | Multi-TRP / Tables 4–5 | 比较同时改变TRP协调/层数；不能写成2CW相对1CW的增益。 |
| E005 | Beijing Xinwei Telecom Techn. | TSGR1_88 [R1-1702022](../sources/TSGR1_88/Docs/R1-1702022.zip) | LLS / CW数量及接收机 | 2CW+SSD-SIC、2CW+MMSE-SIC；基线：1CW+SSD、1CW+MMSE | 2CW+SSD-SIC最好；1CW+SSD优于2CW+MMSE-SIC；正文无数值差 | EVA/ideal CE；rank1/2；QPSK R0.6 | Evaluation Results / Annex / figure | 跨接收机比较；不能全部归因于CW数量。 |
| E006 | Intel Corporation | TSGR1_88 [R1-1702187](../sources/TSGR1_88/Docs/R1-1702187.zip) | SLS / CW数量 | Rank1/2均1CW；基线：Rank1=1CW、Rank2=2CW | mean UPT +4/+5/+6/+7%；5%-UPT +5/+7/+8/+10% | UMa/4GHz/10MHz；2Rx；MMSE-IRC；FTP λ60/54～120/54；PF；OLLA10% | SU-MIMO / Table 1 / Appendix |  |
| E007 | Intel Corporation | TSGR1_88 [R1-1702187](../sources/TSGR1_88/Docs/R1-1702187.zip) | SLS统计 / NC-JT适用性 | NC-JT层数选择统计；基线：不是1CW/2CW吞吐量对照 | 4Rx相关统计中两层NC-JT占1/2/4/8%，3/4层占99/98/96/92%；不能当增益 | Indoor 8small cells；2Tx X-pol；2/4Rx；FTP | NC-JT / Tables 2–3 | 是模式选择统计，不是映射方案性能增益。 |
| E008 | AT&T | TSGR1_88 [R1-1702261](../sources/TSGR1_88/Docs/R1-1702261.zip) | LLS / CW数量 | 1/2/3CW相对4CW上界；基线：4CW（每层独立CQI/MCS） | 1CW损失约19%(10dB)、20%(25dB)；2CW高SNR损失约7%；3CW约2% | 4ports；TDL-A/3kmh；Turbo/LTE R8 codebook；ideal CE、控制开销0、反馈延迟4TTI | Simulation Results with 4 Antenna Ports / Figures 1–4 | 原文以4CW作分母的loss；反向增益不能照搬同一百分比。 |
| E009 | AT&T | TSGR1_88 [R1-1702261](../sources/TSGR1_88/Docs/R1-1702261.zip) | LLS / CW数量 | 1CW相对2CW；基线：2CW | 2ports/25dB：1CW约损失13%；4ports限制rank≤2：中高SNR约损失9% | 同文Table1；closed-loop/adaptive PMI/RI/MCS；ideal CE；未计控制开销 | Simulation Results with 2 Antenna Ports / Rank Restriction / Figures 5–7 |  |
| E010 | AT&T | TSGR1_88 [R1-1702262](../sources/TSGR1_88/Docs/R1-1702262.zip) | LLS / 灵活空间层分组 | 2CW动态选择rank4层分组{12/34,13/24,14/23}；基线：2CW固定{12/34} | SE约+12%（作者正文近似值） | 固定rank4；4ports；TDL-A/3kmh；ideal CE/0控制开销；Turbo | Codeword to Layer Mapping Options / Figures 1–2 | 纯分组对照较直接；实测净开销收益未给出。 |
| E011 | AT&T | TSGR1_88 [R1-1702263](../sources/TSGR1_88/Docs/R1-1702263.zip) | LLS / TB/CW处理结构 | 一个CW含多个TB；可做CW内部SIC；基线：LTE两个CW、每CW一个TB | 不加advanced RX时性能相同；SIC例子有曲线，正文无统一数值 | 4ports/TDL-A/3kmh；Turbo；ideal CE；0控制开销 | Simulation Results / Figures 1–2 | 此处TB/CW定义属于作者提案，不能当NR最终定义。 |
| E012 | Qualcomm Incorporated | TSGR1_88 [R1-1702596](../sources/TSGR1_88/Docs/R1-1702596.zip) | LLS / CW内分层调制 | 1CW内每层可用不同QAM阶数；基线：1CW所有层同QAM | 30GHz rank2约1.5dB、rank4约7～8dB；相对2/4CW差距很小 | CDL-C300ns rank2、CDL-B100ns rank4；120kHz/64RB；随机UE朝向、双panel | Performance evaluation / Figures 8–9 | 这是调制适配的链路SNR收益，不能当增加CW的SLS百分比收益。 |
| E013 | Qualcomm Incorporated | TSGR1_88 [R1-1702596](../sources/TSGR1_88/Docs/R1-1702596.zip) | LLS / CW数量/分层调制 | SCW+分层调制；基线：MCW(2CW/4CW)；另有SCW同调制 | sub6 rank2/4/8：分层调制恢复多数单CW损失，接近MCW；无统一百分比 | 16x8；30kHz/84PRB；CDL-B100ns/CDL-C300ns；实际SRS/DMRS估计、SVD | Performance evaluation / Figures 1–7 |  |
| E014 | Ericsson | TSGR1_88 [R1-1702669](../sources/TSGR1_88/Docs/R1-1702669.zip) | SLS / CW数量 | LTE最多2CW / 每层1CW；基线：所有层共用1CW | 2Rx：2CW mean -5/-4%、edge -4/-11%；4Rx：2CW mean -1/-5%；8Rx：2CW mean 0/-3%；每层CW可差至mean -15%、edge -31% | UMi2GHz/10MHz；RU20/50%；MMSE；57cells；CSI5ms+delay5ms；FTP/PF/OLLA | Simulation results / Tables 1–3 / Appendix | 正负号均相对单CW。 |
| E015 | Samsung | TSGR1_88 [R1-1702916](../sources/TSGR1_88/Docs/R1-1702916.zip) | SLS / CW数量 | LTE最多2CW；基线：单CW symbol-level mapping（表中100%） | 各rank上限2/4/8、16/32ports、SU/MU：2CW平均为1CW的94.9～98.4%；5%-UPT为87.1～95.6% | UMi2GHz；非fullbuffer λ4；SLNR/PF/MMSE-IRC；实际CE/CSI | Tables 1–3 / Appendix | 表头gain是相对值（100%=基准），不是+94.9%增益。 |
| E016 | Nokia, Alcatel-Lucent Shanghai Bell | TSGR1_88 [R1-1703150](../sources/TSGR1_88/Docs/R1-1703150.zip) | SLS / NC-JT及CW/接收机组合 | NC-JT单CW vs 不同CW/数据流，MMSE或CWIC；基线：单小区SU-MIMO；并给NC-JT各分支 | Indoor mean 27.0→31.9(单CW NCJT)→34.2(不同流/CW)Mbps；3DUMi低负载51.4→53.2→55.8；高负载25.2→28.6→28.4 | 2Tx AP/4Rx；各TRP≤2层，总≤4层；bursty traffic | System performance / Figure2 / Appendix Table3 | 原表同时改变JT/流/接收机且RU不等；不是独立映射收益，edge二维单元需原表复核。 |
| E017 | AT&T | TSGR1_88b [R1-1704335](../sources/TSGR1_88b/Docs/R1-1704335.zip) | LLS / CW数量/灵活层分组 | 与#88相同的多CW及动态分组；基线：4CW上界；固定2CW分组 | 重述1CW损失约19～20%、2CW损失7%、动态分组约12% | 与R1-1702261/2262近似同组假设 | Figures 1–7 / Codeword to Layer Mapping Options | 复用#88结果，不计作独立数据集。 |
| E018 | ZTE, ZTE Microelectronics | TSGR1_88b [R1-1704390](../sources/TSGR1_88b/Docs/R1-1704390.zip) | SLS / 单CW内每层LA | 文中标为1CW with per-layer link adaptation；基线：1CW without per-layer link adaptation | Tables1–3与R1-1701790数值一致：mean +3.72～13.33%、MU avg SE +2.96%等 | Indoor/UMi；表内仍使用每层MCS和重传论证 | Per-layer link adaptation / Tables1–3 | 数值复用但方案标签由2CW改为per-layer LA；不足以认定新增独立测量。 |
| E019 | Beijing Xinwei Telecom Techn. | TSGR1_88b [R1-1704661](../sources/TSGR1_88b/Docs/R1-1704661.zip) | LLS / 空间/频率映射顺序 | 频率先、再层、最后时间(含layer shift)；基线：层先映射；MMSE/SSD及SIC对照 | 正文定性：频率先支持SIC有收益，layer shift补分集；未给数字 | CDL-A/ideal CE；SU-MIMO；MMSE/SSD/MMSE-SIC/SSD-SIC | Evaluation Results / two figures / Annex | 未读图量化时不能补造dB。 |
| E020 | Intel Corporation | TSGR1_88b [R1-1704717](../sources/TSGR1_88b/Docs/R1-1704717.zip) | SLS / rank3/4的CW数量 | rank3/4用1CW；基线：rank3/4用2CW；两分支rank1/2均1CW | EMF表：mean 69.83→70.19、66.28→66.72、63.03→63.50Mbps（作者均标+1%）；5%-UPT标+2/+1/+1% | MMSE-IRC；λ40/60/80每秒；RU约4.1/6.2/8.6%；很低负载 | SU-MIMO performance for rank 3 and 4 / Table1 (3 EMF images) | 已将三幅原EMF渲染核对；百分比为作者取整，绝对数值保留。 |
| E021 | Huawei, HiSilicon | TSGR1_88b [R1-1705073](../sources/TSGR1_88b/Docs/R1-1705073.zip) | SLS / CW数量 | rank4用2CW（2-to-4）；基线：rank4用1CW（1-to-4） | Figure1：mean +15.04/+17.00/+17.47%；median +25.23/+35.20/+42.32%；5% +57.33/+68.65/+51.23% | 图注SU-MIMO、8T8R、Dense Urban、Rank=4；λ1.2/2.4/5.2；4GHz/10MHz | Discussion on codeword number / Figure1 / Appendix Table1 | 原PNG已核对：正文43.2%与图中42.32%不一致，采用图值；图为固定rank4，非所有≤4层平均。 |
| E022 | Huawei, HiSilicon | TSGR1_88b [R1-1705073](../sources/TSGR1_88b/Docs/R1-1705073.zip) | SLS / NC-JT/多panel | 2CW及CW-SIC/PIC；基线：1CW及singleTRP2CW参考 | NC-JT、多panel有显著收益；正文无统一百分比 | ≤4layers；distributed precoding；panel间无联合预编码；IC类型会变 | Figures2–3,11 / Discussion on codeword number | 接收机/协调也改变，不能当纯映射增益。 |
| E023 | Huawei, HiSilicon | TSGR1_88b [R1-1705073](../sources/TSGR1_88b/Docs/R1-1705073.zip) | LLS / 资源映射/交织 | 时频联合交织Pattern3；基线：LTE L-F-T不交织Pattern1；仅频域Pattern2 | 高速Pattern3较好；30MHz/120kmh Pattern1/2近重合；正文无dB | CDL-A100ns；4GHz；30/60MHz；3/120kmh；64QAM5/6、16QAM3/4；1layer/1CW | Mapping patterns / Figures7–9 / Appendix Table2 | 表2为单层，不是多层分组收益。 |
| E024 | Samsung | TSGR1_88b [R1-1705333](../sources/TSGR1_88b/Docs/R1-1705333.zip) | SLS / CW数量 | 最多2CW；基线：最多1CW（表中100%） | rank≤4：2CW平均为1CW的96.1～98.6%；低负载λ2.5的edge为91.0～92.0% | 16/32ports SU/MU；UMi2GHz；λ4与2.5；实际CE/CSI；MMSE-IRC | Appendix A / Tables1–2 | λ4部分复用R1-1702916，λ2.5为新增负载；不是独立重复投票。 |
| E025 | Samsung | TSGR1_88b [R1-1705333](../sources/TSGR1_88b/Docs/R1-1705333.zip) | SLS / CW shifting | rank>4双CW之间shifting ON，1MCS/1HARQ；基线：shifting OFF，2MCS/2HARQ | 原表OFF/ON：mean98.2～99.1%、5%-UPT86.5～91.1%；中位数部分OFF略优 | rank≤4均1CW；最高8层；λ4/2.5；16/32ports SU/MU | Appendix B / Tables3–4 | 保留OFF/ON原表方向；不能把98%写成98%增益。 |
| E026 | Qualcomm Incorporated | TSGR1_88b [R1-1705574](../sources/TSGR1_88b/Docs/R1-1705574.zip) | LLS+推估 / 分层调制 | SCW per-layer QAM；基线：SCW common QAM | sub6：用LLS曲线×几何CDF推估8x4 fullbuffer mean SE约+7%；mmW重述rank2 1.5dB/rank4 7～8dB | CDL-B100ns；realistic SRS/DMRS；SVD；16x4/8x4/4x4；4GHz宏几何CDF | Performance results / Figures1–7 | 7%是LLS结合CDF推算，不能标成独立动态SLS。mmW重复#88。 |
| E027 | Lenovo, Motorola Mobility | TSGR1_88b [R1-1705649](../sources/TSGR1_88b/Docs/R1-1705649.zip) | SLS统计 / 多panel适用性 | 单TRP双panel相干传输+panel间频率平坦相位误差；基线：无CW数量对照 | rank3/4约50%传输；rank4超过30% UE最强/最弱奇异值差>10dB；不提供吞吐增益 | UMi2GHz/10MHz；fullbuffer；4x4双极化panel→8ports/panel；SVD/MMSE/ideal CE | Number of Codewords for 3 and 4 Layers / Figures2–3 / Appendix1 | 仅秩/条件数统计，不能报告为映射gain。 |
| E028 | Ericsson | TSGR1_88b [R1-1705883](../sources/TSGR1_88b/Docs/R1-1705883.zip) | SLS / rank3/4的CW数量 | Alt2：rank3/4用2CW；基线：Alt1：rank3/4用1CW | 2CW相对1CW：normalized UPT +1/+4/+3/-2%；edge -1/+4/+4/-3% | UMi2GHz/10MHz/RU50%；8/32BS ports×4/8Rx；MMSE；OLLA10% | On the number of codewords / Tables1–4 |  |
| E029 | Intel Corporation | NR_AH_1701 [R1-1700338](../sources/NR_AH_1701/Docs/R1-1700338.zip) | SLS / CW数量 | Rank≤2用1CW；基线：Rank2用2CW | Table1的mean +4～7%、5%-UPT +5～10%（#88 R1-1702187复用） | UMa4GHz/10MHz、2Rx、MMSE-IRC；FTP多负载 | SU-MIMO / Table1 | 先于#88；两文不算独立数据集。 |
| E030 | Huawei, HiSilicon | NR_AH_1701 [R1-1700412](../sources/NR_AH_1701/Docs/R1-1700412.zip) | SLS / CW数量 | Rank2双CW；基线：Rank2单CW | MU-MIMO作者报告mean最多+20%、median+32%、5%-UPT+28% | Dense urban/4GHz/10MHz；57TRPs；FTP；MMSE-IRC | 2 MIMO layers / Figure1 / Appendix Table1 | 各指标最大值不一定同负载；图与正文若有取整差异保留原图。 |
| E031 | Huawei, HiSilicon | NR_AH_1701 [R1-1700412](../sources/NR_AH_1701/Docs/R1-1700412.zip) | SLS / 高秩CW数量 | Rank4的2CW；Rank8的1/2/4CW；基线：Rank4图以2CW为基准；Rank8以4CW为基准 | 作者描述rank4的2CW较1CW mean最多+20%、较4CW最多差1%；rank8的1CW/2CW较4CW mean损失最多59%/37% | 同文SLS；固定rank4/8对照 | 3–8 MIMO layers / Figures3–4 | rank4正文gain与图归一化分母需分辨；rank8损失以4CW作分母。 |
| E032 | Beijing Xinwei Telecom Techn. | NR_AH_1701 [R1-1700777](../sources/NR_AH_1701/Docs/R1-1700777.zip) | LLS / CW数量/接收机 | 1CW SSD；2CW MMSE-SIC；基线：相应MMSE以及其他接收机 | 1CW SSD优于2CW MMSE-SIC；SIC优于MMSE；正文无dB | CDL-A100ns/3kmh；ideal SVD/CE；rank1/2、QPSK R0.6 | Evaluation Results / Annex | 与#88 Xinwei文接收机组合不完全相同。 |
| E033 | Samsung | NR_AH_1701 [R1-1700898](../sources/NR_AH_1701/Docs/R1-1700898.zip) | SLS / CW数量 | 最多2CW LTE mapping；基线：1CW symbol-level mapping | Table3：2CW mean为1CW的98.1～99.2%、5%-UPT为96.6～98.4%；相近 | UMi2GHz；16/32ports、SU/MU、maxrank4；非fullbuffer | Simulation results / Table3 | 表中100%=基准，不是+100%收益。 |
| E034 | Samsung | NR_AH_1701 [R1-1701201](../sources/NR_AH_1701/Docs/R1-1701201.zip) | SLS / CW数量 | 最多2CW LTE mapping；基线：1CW symbol-level mapping | R1-1700898的修订版，包含后续#88 R1-1702916相同表值 | maxrank2/4/8、16/32ports；UMi2GHz | Simulation results / Tables | 同一会议修订/后续复用，不能作为独立数据集计数。 |
| E035 | Beijing Xinwei Telecom Techn. | TSGR1_89 [R1-1707083](../sources/TSGR1_89/Docs/R1-1707083.zip) | LLS / 空间/频率映射 | FLT含layer shift及SIC；基线：LFT及非SIC | 定性：相同接收机差距有限；子载波先映射支持SIC增益；未给统一数字 | Annex仿真假设；参考原曲线 | Evaluation Results / Annex | 部分接收机/曲线与R1-1704661延续。 |
| E036 | AT&T | TSGR1_89 [R1-1707737](../sources/TSGR1_89/Docs/R1-1707737.zip) | LLS / 灵活空间层分组 | rank8双CW动态分组；基线：rank8双CW固定分组 | SE约+18%@20dB、+15%@25dB；rank4另给曲线 | 8ports、fixed rank8；TDL-A3kmh、ideal CE、4TTI反馈 | Dynamic layer mapping / Figures1–4 / Table1 |  |
| E037 | AT&T | TSGR1_89 [R1-1707737](../sources/TSGR1_89/Docs/R1-1707737.zip) | SLS / 灵活空间层分组 | 双CW动态分组；基线：双CW固定分组 | average sector throughput约+11%；90% throughput约+10% | 3D UMa2GHz/5MHz；57TRPs、10UE；fullbuffer；SU-MIMO/MMSE-IRC | System Level Simulation Results / Figure5 / Table2 | 90%是原文用语，勿改为cell-edge。 |
| E038 | AT&T | TSGR1_89 [R1-1707737](../sources/TSGR1_89/Docs/R1-1707737.zip) | LLS / 频域交织 | 每OFDM symbol/每层随机交织；基线：无符号频域交织 | 3kmh/50PRB仅高SNR约2%；120kmh改善主要在高SNR；1/2PRB近无收益 | 4x4、1CW；conventional LA对交织透明 | Frequency interleaver / Figures6–9 |  |
| E039 | Huawei, HiSilicon | TSGR1_89 [R1-1708128](../sources/TSGR1_89/Docs/R1-1708128.zip) | LLS / 频域交织 | 仅频域per-symbol交织；基线：无额外交织 | 64QAM/3kmh四种配置：10%BLER收益≤0.4dB；QPSK/16QAM可无收益 | CDL-A1000ns；20/60MHz；rank1/2/4、2–4CB/symbol | Simulation first part / Figure2 / Table2 |  |
| E040 | Huawei, HiSilicon | TSGR1_89 [R1-1708128](../sources/TSGR1_89/Docs/R1-1708128.zip) | LLS / 时频交织 | 跨多个OFDM symbol联合交织；基线：无交织/仅频域交织 | 60/120kmh约3dB@10%BLER；380kmh时前两者出现误码平台，联合方案约14dB达到10%BLER | 4GHz；CDL-A1000ns；30MHz、16QAM3/4或64QAM5/9；rank1 | Simulation second/third part / Figures3–4 | 14dB是达到目标的绝对SNR，不能当14dB增益。 |
| E041 | Qualcomm Incorporated | TSGR1_89 [R1-1708579](../sources/TSGR1_89/Docs/R1-1708579.zip) | LLS / 频域交织 | row-column 4-tone inter-CB交织；基线：仅intra-CB交织、无inter-CB频域交织 | 64QAM8/9：0.1～2dB；256QAM8/9：0.7～>5dB@10%TBLER；取决于PRB与信道 | LDPC8192bits；4x4 rank4 SCW；30kHz；45/85/170/275PRB；TDL-B100ns/C300ns | Performance Evaluations / LDPC table | >5dB是特定256QAM大带宽案例，不代表平均增益。 |
| E042 | ZTE | TSGR1_90 [R1-1712284](../sources/TSGR1_90/Docs/R1-1712284.zip) | SLS / CW内layer-set/CBG映射 | Layer-set1→F→T→Layer-set2→F→T；基线：LFT、CB分散于所有层 | FTP/RU80%：mean+1.44%、5%+11.05%、median+6.13%、95%-0.3%；fullbuffer：cellSE+1.55%、5%-SE+14.13% | Indoor3.5GHz/10MHz；NCJT ideal backhaul；MMSE-IRC/SIC；varying interference | Resource Mapping / Scheme1 / Tables1–2,5 | CBG/OLLA/层集策略一起变化；并非改变CW数量。 |
| E043 | ZTE | TSGR1_90 [R1-1712284](../sources/TSGR1_90/Docs/R1-1712284.zip) | LLS / LTF资源映射 | LTF、增加时间分集；基线：LFT（两者均frequency interleaving） | 300/500kmh作者报告最大性能收益>10%；干扰变化另给定性曲线 | CDL-A4GHz；100PRB/15kHz；16QAM1/2+OLLA；4Tx2Rx、rank adaptation | Scheme2 / Figures2–3 / Table6 | 原文Proposal1后又把scheme2误写为LFT，按讨论段明确的LTF记录。 |
| E044 | Intel Corporation | TSGR1_90 [R1-1712536](../sources/TSGR1_90/Docs/R1-1712536.zip) | LLS / 时频映射顺序 | time-first mapping；基线：frequency-first mapping（另有F-interleaving） | 高速可获收益，低速两例time-first反而较差；无统一数值 | TDL-A30ns；4GHz/15kHz；1layer、16QAM5/9或QPSK2/3；400/约100–120PRB | Time first symbol level mapping / Figures1–2 / Table1 | Table1与Figure2的PRB标注120/100不一致。 |
| E045 | Intel Corporation | TSGR1_90 [R1-1712536](../sources/TSGR1_90/Docs/R1-1712536.zip) | LLS / 频域交织 | per-symbol 3-block交织；基线：无频域交织 | 10%BLER：TDL-A 0.70～0.84dB；TDL-B0.58～0.69dB；TDL-C0.30dB | 1layer；64QAM R2/3、3/4、5/6；约2.9/3.2/3.5CB/symbol；4GHz30kmh | Frequency Interleaving / Table3 |  |
| E046 | Intel Corporation | TSGR1_90 [R1-1712536](../sources/TSGR1_90/Docs/R1-1712536.zip) | LLS / 层间交织函数 | 不同层使用不同频域交织偏移；基线：所有层相同交织函数 | 约0.8dB@BLER0.1 | 2layers；64QAM8/9；TDL-A30ns、LayerOffInc1600 | Frequency Interleaving / Figure6 / simulation changes table |  |
| E047 | Lenovo, Motorola Mobility | TSGR1_90 [R1-1712670](../sources/TSGR1_90/Docs/R1-1712670.zip) | LLS / URLLC puncturing/交织 | 联合频率-时间交织；基线：仅频域交织；另列无puncture参考 | joint相对frequency-only：0.31～3.10dB；相对sequential：由表中SNR loss相减约0.36～4.25dB@CBGER10% | CDL-A；2Tx2Rx SFBC、Turbo；50/100PRB；每CBG随机单symbol被URLLC抢占 | Performance evaluations / Table1 / Appendix | 第二个范围是Derived calculation，两个SNR loss共同以unpunctured为基准；未做动态SLS。 |
| E048 | vivo | TSGR1_90 [R1-1712829](../sources/TSGR1_90/Docs/R1-1712829.zip) | LLS / 时频交织 | frequency-time交织；基线：无交织/仅频域交织 | 正文定性有收益，曲线给出差异；无数字 | 4GHz/15kHz、2Tx2Rx、TDL-A100ns；30/120kmh；ideal及非ideal CE | Simulation Results / two figures | 原假设写6QAM，疑似64QAM笔误；不静默改正。 |
| E049 | ETRI | TSGR1_90 [R1-1713808](../sources/TSGR1_90/Docs/R1-1713808.zip) | LLS / 高速资源映射/交织 | LTF；multi-symbol交织；基线：LFT；无/仅频域交织 | 图示高速BLER改善；正文无统一dB | 30GHz/80MHz/120kHz；500kmh；1layer/16QAM3/4/Turbo；ideal CE+phase noise/CPE补偿 | Mapping order Figure1 / Frequency interleaver Figure2 / Appendix | Observation1把比较双方均写成LTF，按图题LFT vs LTF和Proposal解读；原文笔误保留。 |
| E050 | Qualcomm Incorporated | TSGR1_90 [R1-1713386](../sources/TSGR1_90/Docs/R1-1713386.zip) | LLS / 频域交织 | 4-tone频域交织；基线：无inter-CB交织 | LDPC表重述R1-1708579：0.1～>5dB@10%TBLER；新增500kmh曲线定性 | rank4/LDPC；另有Turbo、170/40PRB、HST | Performance Evaluations / LDPC table / HST Appendix | 同数值表跨会重复，新增HST条件不能视作同一统一百分比。 |
| E051 | Intel Corporation | TSGR1_90b [R1-1717361](../sources/TSGR1_90b/Docs/R1-1717361.zip) | LLS / DFT-s-OFDM hopping资源映射 | Option3：交替跨两个hop映射；基线：Option1：frequency→time→hop | ≥2CB时约1.3～1.8dB@BLER10%；单CB相同 | DFT-s-OFDM/intra-slot FH；表1–3详列MCS | Performance evaluation / Table3 / Observations | 这是单层上行RE/hop映射，不是CW空间层分组。 |
| E052 | ZTE, Sanechips | TSGR1_90b [R1-1717416](../sources/TSGR1_90b/Docs/R1-1717416.zip) | LLS / DFT-s-OFDM hopping资源映射 | Option3；基线：Option1 | 10RB/单CB近同；30/50RB多CB最高约20%（作者报告） | CDL-D、120/500kmh；100RB系统带宽、10/30/50RB分配 | Performance comparison / Figure2 / Table2 | 后续R1-1719526复用同组描述/图。 |
| E053 | NTT DOCOMO, INC. | TSGR1_90b [R1-1718187](../sources/TSGR1_90b/Docs/R1-1718187.zip) | LLS / DFT-s-OFDM hopping资源映射 | Option3及非对称hop修订3+；基线：Option1 frequency-first | 多CB：约1.5～2dB@BLER10%；单CB近相同；3+改善非对称hop的部分例子 | 4GHz/150RB系统、10/50RB分配；QPSK1/2、16QAM1/2、64QAM5/6 | LLS / Figures2,4 / TableA | 正文对3/3+一处有互相矛盾表述，不给3+统一数值。 |
| E054 | MediaTek Inc. | TSGR1_90b [R1-1718335](../sources/TSGR1_90b/Docs/R1-1718335.zip) | LLS / DFT-s-OFDM hopping资源映射 | Option2/3；基线：Option1 | Option1在10%BLER约损失1～2dB；Option3获得多数Option2收益 | 50RB、hop偏移50RB；CQI5/8/14→2/3/6CB/TTI | Frequency hopping gain and time diversity / Figures2–3 / AppendixA |  |
| E055 | AT&T | TSGR1_90b [R1-1718384](../sources/TSGR1_90b/Docs/R1-1718384.zip) | LLS / DFT-s-OFDM hopping资源映射 | Option3；基线：Option1 | Option3更好，高Doppler差距更明显；正文无统一数字 | 4GHz/20MHz；20RB、2CB；TDL-A3/120kmh；Turbo、practical CE；16QAM3/4、64QAM1/2 | Simulation Results / Figures4–6 / Table1 |  |
| E056 | Qualcomm Incorporated | TSGR1_90b [R1-1718535](../sources/TSGR1_90b/Docs/R1-1718535.zip) | LLS / DFT-s-OFDM hopping资源映射 | Option3；基线：Option1；并含LTE-like Option2 | 非重叠hop且>1CB时Option3较优；重叠hop无额外收益且增Tx buffer；无统一数字 | 2Tx2Rx/rank1；TDL-C300ns；10/40/60PRB、hop间gap80PRB；3/120kmh；Turbo/OLLA | RE mapping / Observations1–2 / Appendix | 与#91 R1-1720656跨会复用。 |
| E057 | Huawei, HiSilicon | TSGR1_91 [R1-1719430](../sources/TSGR1_91/Docs/R1-1719430.zip) | LLS / DFT-s-OFDM hopping资源映射 | Option3；基线：Option1 | 多CB时Option3较优，单CB同；正文未给统一数字 | 3/240kmh；hop gap100PRB；DMRS按速度配置 | Comparison / Appendix Figures2–3 | 延续#90bis R1-1717295结果。 |
| E058 | ZTE, Sanechips | TSGR1_91 [R1-1719526](../sources/TSGR1_91/Docs/R1-1719526.zip) | LLS / DFT-s-OFDM hopping资源映射 | Option3；基线：Option1 | 10RB近同，多CB最高约20% | CDL-D120/500kmh；10/30/50RB | Figure2 / Table2 | R1-1717416延续，非独立数据集。 |
| E059 | NTT DOCOMO, INC. | TSGR1_91 [R1-1720798](../sources/TSGR1_91/Docs/R1-1720798.zip) | LLS / DFT-s/CP-OFDM hopping资源映射 | Option3/3+；基线：Option1 | DFT-s多CB约1.5～2dB@BLER10%；进一步研究CP-OFDM | 4GHz；150RB系统、10/50RB；QPSK1/2、16QAM1/2、64QAM5/6 | LLS / Figures2–5 / TableA | DFT-s数值延续R1-1718187；CP-OFDM不能自动套用同dB范围。 |
| E060 | MediaTek Inc. | NR_AH_1706 [R1-1710815](../sources/NR_AH_1706/Docs/R1-1710815.zip) | LLS / CLI下的空间层组映射 | CBG映射到部分层、组内LFT（Mapping1）；基线：跨所有层LFT（Mapping2），同CSI-A | 同频谱效率所需SNR可差数dB（作者定性）；改为interference-aligned CSI-B进一步改善 | UE-UE cross-link interference；INR15/20/25dB；可适配rank | Simulation results / Figures4–6 | 不是给定数值SLS吞吐增益；CSI-B对照同时改变CSI方案。 |
| E061 | Huawei, HiSilicon | NR_AH_1706 [R1-1710446](../sources/NR_AH_1706/Docs/R1-1710446.zip) | LLS / LTF资源映射 | LTF（Order2）；基线：LFT（Order1） | 高速度例子>2dB@BLER10%；11.5dB处SE+21%/+29% | 60/120kmh；64QAM5/9与16QAM3/4；附表DMRS、非ideal CE | Mapping order / Figure1 / tables | 11.5dB是对比SNR，不是11.5dB增益。 |
| E062 | Huawei, HiSilicon | TSGR1_90 [R1-1712228](../sources/TSGR1_90/Docs/R1-1712228.zip) | LLS / LTF资源映射 | LTF；基线：LFT | TableI：60kmh 1.6～2.0dB；120kmh 2.3～3.4dB；350kmh3.3/4.5dB@10%BLER；CBG重传后约2dB SE曲线横向差 | CDL-A delay100/1000ns；rank1/2；15kHz；16/64QAM；CBG2/4 | Mapping order / TablesI–II / Figure2 / Observations1–7 | 正文写120kmh至少2.5dB，表中rank2/DS1000ns为2.3dB；采用完整表范围。 |
| E063 | Huawei HiSilicon | TSGR1_90 [R1-1714974](../sources/TSGR1_90/Docs/R1-1714974.zip) | LLS / 高速LTF资源映射 | LTF；基线：LFT | 60kmh>1.6dB；120kmh>2.4dB；200kmh>4dB；350kmh>3.3dB；400kmh/30kHz约4dB；均10%BLER | 15/30kHz；不同DMRS、CDL/TDL组合见TablesI–V；rank1/2 | Simulation Results / Figures2–8 / TablesI–V | 为会议内追加Huawei/HiSilicon结果；须按速度/信道逐项看表，不能拼成统一曲线。 |
| E064 | Samsung | NR_AH_1706 [R1-1710642](../sources/NR_AH_1706/Docs/R1-1710642.zip) | LLS / 资源映射顺序 | LFT及其它候选顺序；基线：同条件其他映射顺序 | Appendix图显示LFT属最佳方案之一；无统一数值 | 2GHz/20PRB；4Tx2Rx rank2/1CW；Turbo MCS5、CDL-C100ns、3kmh、MMSE CE | Appendix Figure2 / Table3 | 候选比较同为低速；不能用此单例否定高速场景结果。 |
| E065 | AT&T | NR_AH_1709 [R1-1716174](../sources/NR_AH_1709/Docs/R1-1716174.zip) | LLS / DFT-s-OFDM映射顺序 | Option1频率先 vs Option2时间先；基线：互为对照，含无FH与有FH | 5RB/单CB近同；50RB无FH时Option1较好；有FH：QPSK偏Option1、16QAM可Option2较好；无统一数字 | TDL-A3kmh、20MHz；Turbo；5/50RB | DFT-S-OFDM / Figures1–6 / Table1 |  |
| E066 | AT&T | NR_AH_1709 [R1-1716174](../sources/NR_AH_1709/Docs/R1-1716174.zip) | LLS/链路统计 / 灵活空间层分组 | rank6/7/8及自适应rank的动态分组；基线：固定层分组 | CQI efficiency CDF各例改善，正文未给统一百分比 | 8ports/2CW；基于CSI选择映射，Figures7–10 | Dynamic layer mapping / Figures7–10 | CQI效率统计不是动态SLS吞吐。 |
| E067 | Qualcomm Incorporated | NR_AH_1701 [R1-1700795](../sources/NR_AH_1701/Docs/R1-1700795.zip) | LLS / CW内分层调制 | 1CW内每层可用不同QAM阶数；基线：1CW所有层同QAM | 30GHz rank2约1.5dB、rank4约7～8dB；相对2/4CW差距很小 | CDL-C300ns rank2、CDL-B100ns rank4；120kHz/64RB；随机UE朝向、双panel | Performance evaluation / Figures 8–9 | 跨会/修订重复或延续；参见 R1-1702596。这是调制适配的链路SNR收益，不能当增加CW的SLS百分比收益。 |
| E068 | Huawei, HiSilicon | TSGR1_88 [R1-1703341](../sources/TSGR1_88/Docs/R1-1703341.zip) | SLS / CW数量 | Rank2双CW；基线：Rank2单CW | MU-MIMO作者报告mean最多+20%、median+32%、5%-UPT+28% | Dense urban/4GHz/10MHz；57TRPs；FTP；MMSE-IRC | 2 MIMO layers / Figure1 / Appendix Table1 | 跨会/修订重复或延续；参见 R1-1700412。各指标最大值不一定同负载；图与正文若有取整差异保留原图。 |
| E069 | Samsung | TSGR1_89 [R1-1709231](../sources/TSGR1_89/Docs/R1-1709231.zip) | LLS / 资源映射顺序 | LFT及其它候选顺序；基线：同条件其他映射顺序 | Appendix图显示LFT属最佳方案之一；无统一数值 | 2GHz/20PRB；4Tx2Rx rank2/1CW；Turbo MCS5、CDL-C100ns、3kmh、MMSE CE | Appendix Figure2 / Table3 | 跨会/修订重复或延续；参见 R1-1710642。候选比较同为低速；不能用此单例否定高速场景结果。 |
| E070 | AT&T | NR_AH_1706 [R1-1710426](../sources/NR_AH_1706/Docs/R1-1710426.zip) | LLS / 灵活空间层分组 | rank8双CW动态分组；基线：rank8双CW固定分组 | SE约+18%@20dB、+15%@25dB；rank4另给曲线 | 8ports、fixed rank8；TDL-A3kmh、ideal CE、4TTI反馈 | Dynamic layer mapping / Figures1–4 / Table1 | 跨会/修订重复或延续；参见 R1-1707737。 |
| E071 | Intel Corporation | NR_AH_1706 [R1-1710517](../sources/NR_AH_1706/Docs/R1-1710517.zip) | LLS / 频域交织 | per-symbol 3-block交织；基线：无频域交织 | 10%BLER：TDL-A 0.70～0.84dB；TDL-B0.58～0.69dB；TDL-C0.30dB | 1layer；64QAM R2/3、3/4、5/6；约2.9/3.2/3.5CB/symbol；4GHz30kmh | Frequency Interleaving / Table3 | 跨会/修订重复或延续；参见 R1-1712536。 |
| E072 | ZTE | NR_AH_1706 [R1-1710175](../sources/NR_AH_1706/Docs/R1-1710175.zip) | SLS / CW内layer-set/CBG映射 | Layer-set1→F→T→Layer-set2→F→T；基线：LFT、CB分散于所有层 | FTP/RU80%：mean+1.44%、5%+11.05%、median+6.13%、95%-0.3%；另给末尾symbol受干扰的LLS曲线 | Indoor3.5GHz/10MHz；NCJT ideal backhaul；MMSE-IRC/SIC；varying interference | Resource mapping / Alt1a / Table2 / Figures | 本篇尚无后续R1-1711606/1712284的fullbuffer +14.13%结果，不混用。 |
| E073 | ZTE | NR_AH_1706 [R1-1711606](../sources/NR_AH_1706/Docs/R1-1711606.zip) | SLS / CW内layer-set/CBG映射 | Layer-set1→F→T→Layer-set2→F→T；基线：LFT、CB分散于所有层 | FTP/RU80%：mean+1.44%、5%+11.05%、median+6.13%、95%-0.3%；fullbuffer：cellSE+1.55%、5%-SE+14.13% | Indoor3.5GHz/10MHz；NCJT ideal backhaul；MMSE-IRC/SIC；varying interference | Resource Mapping / Scheme1 / Tables1–2,5 | 跨会/修订重复或延续；参见 R1-1712284。CBG/OLLA/层集策略一起变化；并非改变CW数量。 |
| E074 | Lenovo, Motorola Mobility | NR_AH_1706 [R1-1710594](../sources/NR_AH_1706/Docs/R1-1710594.zip) | LLS / URLLC puncturing/交织 | 联合频率-时间交织；基线：仅频域交织；另列无puncture参考 | joint相对frequency-only：0.9～2.1dB；相对sequential由表相减为0.96～5.20dB@CBGER10% | AWGN、LTE Turbo；50/100PRB；CBG1/2个；每CBG随机symbol受URLLC穿孔 | Simulation results / Tables2–3 / Figures3–9 | 与后续R1-1712670的CDL-A/SFBC评估不同；不得跨文复制0.31～3.1dB范围。第二范围是Derived calculation。 |
| E075 | ETRI | NR_AH_1706 [R1-1710611](../sources/NR_AH_1706/Docs/R1-1710611.zip) | LLS / 高速资源映射/交织 | LTF；multi-symbol交织；基线：LFT；无/仅频域交织 | 图示高速BLER改善；正文无统一dB | 30GHz/80MHz/120kHz；500kmh；1layer/16QAM2/3/Turbo；TDL-D10ns、ideal CE、phase noise补偿 | Mapping order Figure1 / Frequency interleaver Figure2 / Appendix Table1 | 后续R1-1713808变更MCS等假设，不能当完全同一试验。原Observation1比较对象笔误保留。 |
| E076 | Qualcomm Incorporated | NR_AH_1706 [R1-1711152](../sources/NR_AH_1706/Docs/R1-1711152.zip) | LLS / 频域交织 | row-column 4-tone inter-CB交织；基线：仅intra-CB交织、无inter-CB频域交织 | 64QAM8/9：0.1～2dB；256QAM8/9：0.7～>5dB@10%TBLER；取决于PRB与信道 | LDPC8192bits；4x4 rank4 SCW；30kHz；45/85/170/275PRB；TDL-B100ns/C300ns | Performance Evaluations / LDPC table | 跨会/修订重复或延续；参见 R1-1708579。>5dB是特定256QAM大带宽案例，不代表平均增益。 |
| E077 | Beijing Xinwei Telecom Techn. | NR_AH_1706 [R1-1709904](../sources/NR_AH_1706/Docs/R1-1709904.zip) | LLS / 空间/频率映射 | FLT含layer shift及SIC；基线：LFT及非SIC | 定性：相同接收机差距有限；子载波先映射支持SIC增益；未给统一数字 | Annex仿真假设；参考原曲线 | Evaluation Results / Annex | 跨会/修订重复或延续；参见 R1-1707083。部分接收机/曲线与R1-1704661延续。 |
| E078 | AT&T | TSGR1_90 [R1-1712703](../sources/TSGR1_90/Docs/R1-1712703.zip) | LLS / 灵活空间层分组 | rank8双CW动态分组；基线：rank8双CW固定分组 | SE约+18%@20dB、+15%@25dB；rank4另给曲线 | 8ports、fixed rank8；TDL-A3kmh、ideal CE、4TTI反馈 | Dynamic layer mapping / Figures1–4 / Table1 | 跨会/修订重复或延续；参见 R1-1707737。 |
| E079 | ZTE, Sanechips | NR_AH_1709 [R1-1715430](../sources/NR_AH_1709/Docs/R1-1715430.zip) | LLS / DFT-s-OFDM hopping资源映射 | 时间先无hop scheme2-1、交替型scheme3-1；基线：频率先无hop scheme1-1；另对照增加intra-slot hop | 无hop排序scheme2-1>3-1>1-1，scheme2-1相对1-1最高41%；高速引入hop可能因DMRS时间密度降低而变差 | CDL-D/DFT-s-OFDM；4GHz/20MHz；10/30/50RB；16QAM1/2；120/500kmh；1Tx1Rx | CW to resource mapping / Figures2–4 / Appendix Table2 | 后续R1-1717416/1719526的Option3 +20%不是本篇同一个比较；本篇41%为无hop方案比较。 |
| E080 | MediaTek Inc. | NR_AH_1709 [R1-1716208](../sources/NR_AH_1709/Docs/R1-1716208.zip) | LLS / DFT-s-OFDM hopping资源映射 | Option2/3；基线：Option1 | Option1在10%BLER约损失1～2dB；Option3获得多数Option2收益 | 50RB、hop偏移50RB；CQI5/8/14→2/3/6CB/TTI | Frequency hopping gain and time diversity / Figures2–3 / AppendixA | 跨会/修订重复或延续；参见 R1-1718335。 |
| E081 | Intel Corporation | NR_AH_1709 [R1-1716284](../sources/NR_AH_1709/Docs/R1-1716284.zip) | LLS / DFT-s-OFDM hopping资源映射 | Option3：交替跨两个hop映射；基线：Option1：frequency→time→hop | ≥2CB时约1.3～1.8dB@BLER10%；单CB相同 | DFT-s-OFDM/intra-slot FH；表1–3详列MCS | Performance evaluation / Table3 / Observations | 跨会/修订重复或延续；参见 R1-1717361。这是单层上行RE/hop映射，不是CW空间层分组。 |
| E082 | Qualcomm Incorporated | NR_AH_1709 [R1-1716387](../sources/NR_AH_1709/Docs/R1-1716387.zip) | LLS / DFT-s-OFDM hopping资源映射 | Option3；基线：Option1；并含LTE-like Option2 | 非重叠hop且>1CB时Option2/3相近并优于Option1；Option2显著增加UE Tx buffer；无统一数字 | 2Tx2Rx/rank1；TDL-C300ns；10/40/60PRB、hop间gap80PRB；3/120kmh；Turbo/OLLA | RE mapping / Observations1–2 / Appendix | 本篇未以重叠hop试验支持后续文档的Observation2，分别记录。 |
| E083 | Huawei, HiSilicon | TSGR1_90b [R1-1717295](../sources/TSGR1_90b/Docs/R1-1717295.zip) | LLS / DFT-s-OFDM hopping资源映射 | Option3；基线：Option1 | 多CB时Option3较优，单CB同；正文未给统一数字 | 3/240kmh；hop gap100PRB；DMRS按速度配置 | Comparison / Appendix Figures2–3 | 跨会/修订重复或延续；参见 R1-1719430。延续#90bis R1-1717295结果。 |
| E084 | Qualcomm Incorporated | TSGR1_91 [R1-1720656](../sources/TSGR1_91/Docs/R1-1720656.zip) | LLS / DFT-s-OFDM hopping资源映射 | Option3；基线：Option1；并含LTE-like Option2 | 非重叠hop且>1CB时Option3较优；重叠hop无额外收益且增Tx buffer；无统一数字 | 2Tx2Rx/rank1；TDL-C300ns；10/40/60PRB、hop间gap80PRB；3/120kmh；Turbo/OLLA | RE mapping / Observations1–2 / Appendix | 跨会/修订重复或延续；参见 R1-1718535。与#91 R1-1720656跨会复用。 |
| E085 | Nokia, Alcatel-Lucent Shanghai Bell | TSGR1_88b [R1-1705952](../sources/TSGR1_88b/Docs/R1-1705952.zip) | SLS / 多panel/CW数量 | 最多2CW或4CW；基线：单CW、最高4层 | 多CW的mean/edge均略降；正文无统一百分比 | NR-UMa30GHz；TRP/UE各4sub-panels、8RF beam ports；EBF-WB基于reciprocity | System level simulation / Figure4 (正文误称Figure5) | 相干wideband eigenbeamforming；与不相干、panel间SINR差大的案例条件不同。 |
| E086 | Qualcomm Incorporated | TSGR1_88 [R1-1702597](../sources/TSGR1_88/Docs/R1-1702597.zip) | LLS / 频域交织 | per-tone(K1)/per4tone(K4)交织；基线：无频域交织 | 中高SNR有明显吞吐收益，正文无统一数字 | 3GPP Turbo；4Tx4Rx open-loop SCW；30kHz/170RB=61.2MHz；realistic CE；rank/LA | Simulation results / throughput figures | 本篇为Turbo评估，不能直接套用后续LDPC表的>5dB。 |
| E087 | Huawei, HiSilicon | NR_AH_1709 [R1-1716723](../sources/NR_AH_1709/Docs/R1-1716723.zip) | LLS / DFT-s-OFDM资源映射 | Option2时间先；基线：Option1；Option3另作对照 | 无FH/240kmh约+1dB；有FH/3kmh：Option2/3较Option1>1.5dB、Option2较3约0.8dB；有FH/240kmh：2较1约1.6dB、较3约0.8dB | 4GHz/50RB/15kHz；CDL-A1000ns；2Tx4Rx rank1；hop gap100RB、非对称hop；nonideal CE | Simulation results / Figures3–8 / Appendix TableI | 此为NR AH3修订结果，未把最初R1-1715459分析文误算为仿真。 |
| E088 | Huawei, HiSilicon | TSGR1_90 [R1-1713765](../sources/TSGR1_90/Docs/R1-1713765.zip) | LLS / 高速LTF/交织 | LTF及multi-symbol交织；基线：LFT；无/单symbol交织 | LTF：60kmh>1.6dB、120kmh>2.4dB、350kmh>3.3dB@10%BLER；有CBG HARQ仍约2dB；仅频交织正文≤0.6dB，结论称<0.5dB | 15kHz；additional DMRS；rank1/2与多MCS，见TablesI–III | Mapping order / Figures2–8 / tables | 同会R1-1714974进一步扩展到200kmh和400kmh/30kHz；原文0.6/0.5差异保留。 |
| E089 | Nokia, Alcatel-Lucent Shanghai Bell | NR_AH_1701 [R1-1701071](../sources/NR_AH_1701/Docs/R1-1701071.zip) | SLS / NC-JT及CW/接收机组合 | NC-JT单CW vs 不同CW/数据流，MMSE或CWIC；基线：单小区SU-MIMO；并给NC-JT各分支 | Indoor mean 27.0→31.9(单CW NCJT)→34.2(不同流/CW)Mbps；3DUMi低负载51.4→53.2→55.8；高负载25.2→28.6→28.4 | 2Tx AP/4Rx；各TRP≤2层，总≤4层；bursty traffic | System performance / Figure2 / Appendix Table3 | 跨会/修订重复或延续；参见 R1-1703150。原表同时改变JT/流/接收机且RU不等；不是独立映射收益，edge二维单元需原表复核。 |
| E090 | Qualcomm Incorporated | TSGR1_89 [R1-1708641](../sources/TSGR1_89/Docs/R1-1708641.zip) | LLS / 频域交织 | row-column 4-tone inter-CB交织；基线：仅intra-CB交织、无inter-CB频域交织 | 64QAM8/9：0.1～2dB；256QAM8/9：0.7～>5dB@10%TBLER；取决于PRB与信道 | LDPC8192bits；4x4 rank4 SCW；30kHz；45/85/170/275PRB；TDL-B100ns/C300ns | Performance Evaluations / LDPC table | 跨会/修订重复或延续；参见 R1-1708579。>5dB是特定256QAM大带宽案例，不代表平均增益。 |
| E091 | Qualcomm Incorporated | TSGR1_89 [R1-1709200](../sources/TSGR1_89/Docs/R1-1709200.zip) | LLS / 频域交织 | row-column 4-tone inter-CB交织；基线：仅intra-CB交织、无inter-CB频域交织 | 64QAM8/9：0.1～2dB；256QAM8/9：0.7～>5dB@10%TBLER；取决于PRB与信道 | LDPC8192bits；4x4 rank4 SCW；30kHz；45/85/170/275PRB；TDL-B100ns/C300ns | Performance Evaluations / LDPC table | 跨会/修订重复或延续；参见 R1-1708579。>5dB是特定256QAM大带宽案例，不代表平均增益。 |
| E092 | MediaTek Inc. | TSGR1_89 [R1-1709193](../sources/TSGR1_89/Docs/R1-1709193.zip) | LLS / CLI下的空间层组映射 | CBG映射到部分层、组内LFT（Mapping1）；基线：跨所有层LFT（Mapping2），同CSI-A | 同频谱效率所需SNR可差数dB（作者定性）；改为interference-aligned CSI-B进一步改善 | UE-UE cross-link interference；INR15/20/25dB；可适配rank | Simulation results / Figures4–6 | 跨会/修订重复或延续；参见 R1-1710815。不是给定数值SLS吞吐增益；CSI-B对照同时改变CSI方案。 |
| E093 | MediaTek Inc. | TSGR1_90 [R1-1713688](../sources/TSGR1_90/Docs/R1-1713688.zip) | LLS / CLI下的空间层组映射 | CBG映射到部分层、组内LFT（Mapping1）；基线：跨所有层LFT（Mapping2），同CSI-A | 同频谱效率所需SNR可差数dB（作者定性）；改为interference-aligned CSI-B进一步改善 | UE-UE cross-link interference；INR15/20/25dB；可适配rank | Appendix A / A.4 Simulation results / Figures | 跨会/修订重复或延续；参见 R1-1710815。不是给定数值SLS吞吐增益；CSI-B对照同时改变CSI方案。 |

## 原文摘录及导航

### E001 — R1-1612738

支持研究SCW以降低控制开销及流水线时延。 [抽取文本，L75](../sources/TSGR1_87/Docs/R1-1612738.txt#L75) · [3GPP官方文件](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_87/Docs/R1-1612738.zip)

> The performance of an SCW and MCW MIMO transmission in Rank 2 CL or OL scenarios can be similar.

### E002 — R1-1701790

多CW可利用层间质量差异；结果依赖负载、CSI和调度。 [抽取文本，L141](../sources/TSGR1_88/Docs/R1-1701790.txt#L141) · [3GPP官方文件](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_88/Docs/R1-1701790.zip)

> significant performance gain of MCW scheme has been observed in both SU and MU-MIMO

### E003 — R1-1701790

每层MCS及重传避免好层被差层拖累。 [抽取文本，L75](../sources/TSGR1_88/Docs/R1-1701790.txt#L75) · [3GPP官方文件](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_88/Docs/R1-1701790.zip)

> Performance of SCW and MCW can highly depend on various factors

### E004 — R1-1701790

NC-JT有收益，不能据此隔离CW映射本身的增益。 [抽取文本，L149](../sources/TSGR1_88/Docs/R1-1701790.txt#L149) · [3GPP官方文件](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_88/Docs/R1-1701790.zip)

> DPS/DPB (baseline scheme)

### E005 — R1-1702022

应同时考虑1CW和2CW，收益与接收机耦合。 [抽取文本，L77](../sources/TSGR1_88/Docs/R1-1702022.txt#L77) · [3GPP官方文件](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_88/Docs/R1-1702022.zip)

> single codeword SSD outperforms two codewords MMSE-SIC

### E006 — R1-1702187

单CW在相似层SINR和稳健LA下稍优。 [抽取文本，L34](../sources/TSGR1_88/Docs/R1-1702187.txt#L34) · [3GPP官方文件](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_88/Docs/R1-1702187.zip)

> single CW provides slightly better performance comparing to two CWs case

### E007 — R1-1702187

作者认为两层NC-JT低频次不足以支撑额外CW。 [抽取文本，L57](../sources/TSGR1_88/Docs/R1-1702187.txt#L57) · [3GPP官方文件](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_88/Docs/R1-1702187.zip)

> NC-JT optimization, such as support of two CWs, is not required for two MIMO layers

### E008 — R1-1702261

支持可配置CW，至少2CW降低相对4CW的损失。 [抽取文本，L94](../sources/TSGR1_88/Docs/R1-1702261.txt#L94) · [3GPP官方文件](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_88/Docs/R1-1702261.zip)

> 19% loss in the spectral efficiency compared to 4 codeword MIMO

### E009 — R1-1702261

双CW在作者高SNR测试有优势。 [抽取文本，L122](../sources/TSGR1_88/Docs/R1-1702261.txt#L122) · [3GPP官方文件](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_88/Docs/R1-1702261.zip)

> the loss is around 13 % at high SNR of 25 dB

### E010 — R1-1702262

UE推荐相近SINR层分组，网络选择映射。 [抽取文本，L117](../sources/TSGR1_88/Docs/R1-1702262.txt#L117) · [3GPP官方文件](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_88/Docs/R1-1702262.zip)

> The percentage of gains are around 12 %

### E011 — R1-1702263

寻求可扩展TB结构而非声称固定百分比增益。 [抽取文本，L142](../sources/TSGR1_88/Docs/R1-1702263.txt#L142) · [3GPP官方文件](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_88/Docs/R1-1702263.zip)

> the proposed structure performance is identical with that of LTE two codeword MIMO

### E012 — R1-1702596

SCW加分层调制可接近MCW。 [抽取文本，L165](../sources/TSGR1_88/Docs/R1-1702596.txt#L165) · [3GPP官方文件](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_88/Docs/R1-1702596.zip)

> there is about 7~8dB gain of using SCW with per-layer modulation

### E013 — R1-1702596

主张每grant单CW+分层/分组调制。 [抽取文本，L171](../sources/TSGR1_88/Docs/R1-1702596.txt#L171) · [3GPP官方文件](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_88/Docs/R1-1702596.zip)

> The performance of a SCW and MCW MIMO transmission scheme with per-layer modulation order can be similar.

### E014 — R1-1702669

单CW分集及稳健CSI/LA可能优于多CW。 [抽取文本，L65](../sources/TSGR1_88/Docs/R1-1702669.txt#L65) · [3GPP官方文件](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_88/Docs/R1-1702669.zip)

> using a single CW provides slightly better performance than using multiple CWs

### E015 — R1-1702916

作者认定相近，单CW对CSI误差稍稳健。 [抽取文本，L73](../sources/TSGR1_88/Docs/R1-1702916.txt#L73) · [3GPP官方文件](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_88/Docs/R1-1702916.zip)

> the performance of “I CW” and “2 CWs” are similar

### E016 — R1-1703150

多CW只在部分mean指标有益，edge并不一致。 [抽取文本，L164](../sources/TSGR1_88/Docs/R1-1703150.txt#L164) · [3GPP官方文件](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_88/Docs/R1-1703150.zip)

> there are not gains in cell edge

### E017 — R1-1704335

将可配置CW主张调整至rank>2。 [抽取文本，L128](../sources/TSGR1_88b/Docs/R1-1704335.txt#L128) · [3GPP官方文件](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_88b/Docs/R1-1704335.zip)

> The network should be able to support flexible number of codewords

### E018 — R1-1704390

提出每层调制、共同编码率等选项。 [抽取文本，L167](../sources/TSGR1_88b/Docs/R1-1704390.txt#L167) · [3GPP官方文件](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_88b/Docs/R1-1704390.zip)

> The per-layer link adaption should be supported in NR.

### E019 — R1-1704661

推荐F-L-T；收益受接收机影响。 [抽取文本，L73](../sources/TSGR1_88b/Docs/R1-1704661.txt#L73) · [3GPP官方文件](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_88b/Docs/R1-1704661.zip)

> Mapping across subcarriers first would enable the use of SIC receivers

### E020 — R1-1704717

确认3/4层单CW的working assumption。 [抽取文本，L31](../sources/TSGR1_88b/Docs/R1-1704717.txt#L31) · [3GPP官方文件](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_88b/Docs/R1-1704717.zip)

> single CW provides similar performance comparing to two CWs case for rank 3-4

### E021 — R1-1705073

反对3/4层单CW假设，主张双CW。 [抽取文本，L69](../sources/TSGR1_88b/Docs/R1-1705073.txt#L69) · [3GPP官方文件](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_88b/Docs/R1-1705073.zip)

> up to 43.2% for 50% UPT, 17.47 for mean UPT and 68.65% for 5% UPT

### E022 — R1-1705073

作者认为多CW支持更细LA及CW级IC。 [抽取文本，L75](../sources/TSGR1_88b/Docs/R1-1705073.txt#L75) · [3GPP官方文件](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_88b/Docs/R1-1705073.zip)

> 2 codewords enables CW-SIC receiver to improve performance over one codeword significantly

### E023 — R1-1705073

联合时频交织增强高速分集，纯频交织有适用性限制。 [抽取文本，L139](../sources/TSGR1_88b/Docs/R1-1705073.txt#L139) · [3GPP官方文件](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_88b/Docs/R1-1705073.zip)

> The codeword-to-layer mapping pattern with both time and frequency interleaving is superior in the high speed scenario.

### E024 — R1-1705333

支持3/4层单CW、节省MCS/HARQ反馈。 [抽取文本，L67](../sources/TSGR1_88b/Docs/R1-1705333.txt#L67) · [3GPP官方文件](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_88b/Docs/R1-1705333.zip)

> the gain of 2-CW

### E025 — R1-1705333

CW shifting模拟单CW分集，简化控制而吞吐相近。 [抽取文本，L71](../sources/TSGR1_88b/Docs/R1-1705333.txt#L71) · [3GPP官方文件](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_88b/Docs/R1-1705333.zip)

> CW shifting ON

### E026 — R1-1705574

作者主张per-group-of-layers modulation。 [抽取文本，L125](../sources/TSGR1_88b/Docs/R1-1705574.txt#L125) · [3GPP官方文件](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_88b/Docs/R1-1705574.zip)

> we expect a mean spectral efficiency system gain of the order of 7%

### E027 — R1-1705649

认为rank4双CW值得考虑。 [抽取文本，L75](../sources/TSGR1_88b/Docs/R1-1705649.txt#L75) · [3GPP官方文件](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_88b/Docs/R1-1705649.zip)

> Rank 3-4 is selected in approximately half of transmission intervals.

### E028 — R1-1705883

作者判断相近，确认单CW并不支持额外分层调制。 [抽取文本，L57](../sources/TSGR1_88b/Docs/R1-1705883.txt#L57) · [3GPP官方文件](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_88b/Docs/R1-1705883.zip)

> The performances are very similar for Alt1 (1 CW) and Alt2 (2 CW).

### E029 — R1-1700338

单CW稍优，NC-JT两层模式占比较低。 [抽取文本，L34](../sources/NR_AH_1701/Docs/R1-1700338.txt#L34) · [3GPP官方文件](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_AH/NR_AH_1701/Docs/R1-1700338.zip)

> single CW provides slightly better performance comparing to two CWs case

### E030 — R1-1700412

作者主张2CW以改善每层LA。 [抽取文本，L47](../sources/NR_AH_1701/Docs/R1-1700412.txt#L47) · [3GPP官方文件](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_AH/NR_AH_1701/Docs/R1-1700412.zip)

> 2 codewords can achieve up to 28%, 32% and 20% of gain

### E031 — R1-1700412

rank4偏好2CW，rank8曾提出4CW。 [抽取文本，L71](../sources/NR_AH_1701/Docs/R1-1700412.txt#L71) · [3GPP官方文件](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_AH/NR_AH_1701/Docs/R1-1700412.zip)

> 1 codeword and 2 codewords suffer significant performance loss of up to 59% and 37%

### E032 — R1-1700777

两种CW设计应结合接收机选择。 [抽取文本，L69](../sources/NR_AH_1701/Docs/R1-1700777.txt#L69) · [3GPP官方文件](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_AH/NR_AH_1701/Docs/R1-1700777.zip)

> one codeword SSD outperforms two codeword cases

### E033 — R1-1700898

单CW可避免CSI测量误差敏感及控制开销。 [抽取文本，L113](../sources/NR_AH_1701/Docs/R1-1700898.txt#L113) · [3GPP官方文件](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_AH/NR_AH_1701/Docs/R1-1700898.zip)

> The performance of “I CW” and “2 CWs” are similar.

### E034 — R1-1701201

单CW和双CW相近。 [抽取文本，L33](../sources/NR_AH_1701/Docs/R1-1701201.txt#L33) · [3GPP官方文件](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_AH/NR_AH_1701/Docs/R1-1701201.zip)

> single CW

### E035 — R1-1707083

倾向FLT，指出SIC高时延复杂度。 [抽取文本，L79](../sources/TSGR1_89/Docs/R1-1707083.txt#L79) · [3GPP官方文件](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_89/Docs/R1-1707083.zip)

> mapping across subcarriers first would enable the use of SIC receivers

### E036 — R1-1707737

UE推荐CW内层分组。 [抽取文本，L104](../sources/TSGR1_89/Docs/R1-1707737.txt#L104) · [3GPP官方文件](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_89/Docs/R1-1707737.zip)

> around 18 % for SNR = 20 dB and 15 % at SNR = 25 dB

### E037 — R1-1707737

灵活空间分组可获系统收益。 [抽取文本，L134](../sources/TSGR1_89/Docs/R1-1707737.txt#L134) · [3GPP官方文件](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_89/Docs/R1-1707737.zip)

> around 11% in average sector throughout and 10 % for the 90% throughput

### E038 — R1-1707737

不建议为有限收益增加交织。 [抽取文本，L157](../sources/TSGR1_89/Docs/R1-1707737.txt#L157) · [3GPP官方文件](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_89/Docs/R1-1707737.zip)

> The gain is around 2% at high SNR.

### E039 — R1-1708128

per-symbol交织收益受带宽/MCS/CB数限制。 [抽取文本，L139](../sources/TSGR1_89/Docs/R1-1708128.txt#L139) · [3GPP官方文件](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_89/Docs/R1-1708128.zip)

> no more than 0.4dB at 10-1 of BLER

### E040 — R1-1708128

高速偏好联合时频交织，承担解码等待。 [抽取文本，L157](../sources/TSGR1_89/Docs/R1-1708128.txt#L157) · [3GPP官方文件](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_89/Docs/R1-1708128.zip)

> about 3dB at BLER of 10-1

### E041 — R1-1708579

多个CB/symbol时可获多dB增益。 [抽取文本，L138](../sources/TSGR1_89/Docs/R1-1708579.txt#L138) · [3GPP官方文件](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_89/Docs/R1-1708579.zip)

> dB gains for achieving TBLER=10%

### E042 — R1-1712284

按layer-set集中CBG有利于不均匀干扰及独立重传。 [抽取文本，L99](../sources/TSGR1_90/Docs/R1-1712284.txt#L99) · [3GPP官方文件](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_90/Docs/R1-1712284.zip)

> It outperforms the agreed baseline in the case with varying interference.

### E043 — R1-1712284

动态TDD/高速时LTF有利。 [抽取文本，L126](../sources/TSGR1_90/Docs/R1-1712284.txt#L126) · [3GPP官方文件](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_90/Docs/R1-1712284.zip)

> maximum performance gain is higher than 10%

### E044 — R1-1712536

映射选择难从局部CSI-RS可靠推断。 [抽取文本，L49](../sources/TSGR1_90/Docs/R1-1712536.txt#L49) · [3GPP官方文件](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_90/Docs/R1-1712536.zip)

> the time first mapping performs worse than frequency first mapping at low speeds.

### E045 — R1-1712536

收益与信道及CB数有关。 [抽取文本，L122](../sources/TSGR1_90/Docs/R1-1712536.txt#L122) · [3GPP官方文件](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_90/Docs/R1-1712536.zip)

> The interleaved always performed better than the original

### E046 — R1-1712536

不同层偏移可提高相关信道分集。 [抽取文本，L128](../sources/TSGR1_90/Docs/R1-1712536.txt#L128) · [3GPP官方文件](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_90/Docs/R1-1712536.zip)

> approximately 0.8dB at BLER=0.1

### E047 — R1-1712670

联合交织均衡同CBG中各CB受损程度。 [抽取文本，L124](../sources/TSGR1_90/Docs/R1-1712670.txt#L124) · [3GPP官方文件](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_90/Docs/R1-1712670.zip)

> ranges between 0.31dB to 3.1 dB

### E048 — R1-1712829

支持时频交织并要求权衡缓冲/时延。 [抽取文本，L182](../sources/TSGR1_90/Docs/R1-1712829.txt#L182) · [3GPP官方文件](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_90/Docs/R1-1712829.zip)

> with frequency time interleaving, performance gains are observed.

### E049 — R1-1713808

延迟宽松的高速应用受益于时间分集。 [抽取文本，L79](../sources/TSGR1_90/Docs/R1-1713808.txt#L79) · [3GPP官方文件](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_90/Docs/R1-1713808.zip)

> Multi-OFDM symbol interleaver can further improve BLER performance for high Doppler scenario.

### E050 — R1-1713386

频域收益依赖多个CB/symbol。 [抽取文本，L132](../sources/TSGR1_90/Docs/R1-1713386.txt#L132) · [3GPP官方文件](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_90/Docs/R1-1713386.zip)

> dB gains for achieving TBLER=10%

### E051 — R1-1717361

承认多CB收益，但认为覆盖主场景低阶QAM小带宽多为1CB。 [抽取文本，L75](../sources/TSGR1_90b/Docs/R1-1717361.txt#L75) · [3GPP官方文件](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_90b/Docs/R1-1717361.zip)

> provides ~1.3-1.8dB gain

### E052 — R1-1717416

多CB时Option3有更多时间/频率分集。 [抽取文本，L53](../sources/TSGR1_90b/Docs/R1-1717416.txt#L53) · [3GPP官方文件](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_90b/Docs/R1-1717416.zip)

> with up to 20% gain

### E053 — R1-1718187

倾向Option3以获hop分集，并权衡缓冲/时延。 [抽取文本，L39](../sources/TSGR1_90b/Docs/R1-1718187.txt#L39) · [3GPP官方文件](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_90b/Docs/R1-1718187.zip)

> the frequency diversity gain of approx. 1.5-2 dB

### E054 — R1-1718335

Option3在分集、时延和buffer间折中。 [抽取文本，L65](../sources/TSGR1_90b/Docs/R1-1718335.txt#L65) · [3GPP官方文件](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_90b/Docs/R1-1718335.zip)

> Option-1 has around 1-2dB loss at target BLER 10%

### E055 — R1-1718384

建议有FH时每CB跨hop以获分集。 [抽取文本，L113](../sources/TSGR1_90b/Docs/R1-1718384.txt#L113) · [3GPP官方文件](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_90b/Docs/R1-1718384.zip)

> option 3 is better compared to option 1

### E056 — R1-1718535

收益取决于hop是否重叠和CB数。 [抽取文本，L65](../sources/TSGR1_90b/Docs/R1-1718535.txt#L65) · [3GPP官方文件](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_90b/Docs/R1-1718535.zip)

> Option 3 may demonstrate superior performance compared to Option 1

### E057 — R1-1719430

作者不支持因低速/覆盖主场景而排除多CB收益。 [抽取文本，L73](../sources/TSGR1_91/Docs/R1-1719430.txt#L73) · [3GPP官方文件](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_91/Docs/R1-1719430.zip)

> Option-3 is preferred in multiple code blocks case.

### E058 — R1-1719526

多CB推荐Option3。 [抽取文本，L59](../sources/TSGR1_91/Docs/R1-1719526.txt#L59) · [3GPP官方文件](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_91/Docs/R1-1719526.zip)

> with up to 20% gain

### E059 — R1-1720798

用跨hop分集改善多CB。 [抽取文本，L49](../sources/TSGR1_91/Docs/R1-1720798.txt#L49) · [3GPP官方文件](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_91/Docs/R1-1720798.zip)

> the frequency diversity gain of approx. 1.5-2 dB

### E060 — R1-1710815

CLI干扰集中时分组CBG比把误差扩散到全CB更稳健。 [抽取文本，L231](../sources/NR_AH_1706/Docs/R1-1710815.txt#L231) · [3GPP官方文件](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_AH/NR_AH_1706/Docs/R1-1710815.zip)

> The difference in SNR to achieve the same spectrum efficiency can be several dBs.

### E061 — R1-1710446

时间分集可独立于增加DMRS改善高速。 [抽取文本，L97](../sources/NR_AH_1706/Docs/R1-1710446.txt#L97) · [3GPP官方文件](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_AH/NR_AH_1706/Docs/R1-1710446.zip)

> more than 2 dB gain over the order 1

### E062 — R1-1712228

高速时间分集不能仅由CBG重传替代。 [抽取文本，L118](../sources/TSGR1_90/Docs/R1-1712228.txt#L118) · [3GPP官方文件](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_90/Docs/R1-1712228.zip)

> 4.5 dB and 3.3 dB time diversity gain

### E063 — R1-1714974

增加SCS和additional DMRS后LTF仍有收益。 [抽取文本，L128](../sources/TSGR1_90/Docs/R1-1714974.txt#L128) · [3GPP官方文件](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_90/Docs/R1-1714974.zip)

> Mapping order-2 shows more than 3.3 dB gain

### E064 — R1-1710642

优先流水线及空间分集，灵活对应须再用SLS证明。 [抽取文本，L167](../sources/NR_AH_1706/Docs/R1-1710642.txt#L167) · [3GPP官方文件](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_AH/NR_AH_1706/Docs/R1-1710642.zip)

> Link-level evaluation results on layer mapping schemes

### E065 — R1-1716174

作者因常见场景及pipeline选择Option1。 [抽取文本，L101](../sources/NR_AH_1709/Docs/R1-1716174.txt#L101) · [3GPP官方文件](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_AH/NR_AH_1709/Docs/R1-1716174.zip)

> only one code block is transmitted.

### E066 — R1-1716174

动态层分组能改善CQI效率。 [抽取文本，L203](../sources/NR_AH_1709/Docs/R1-1716174.txt#L203) · [3GPP官方文件](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_AH/NR_AH_1709/Docs/R1-1716174.zip)

> the dynamic layer mapping gives gains compared to fixed layer mapping.

### E067 — R1-1700795

SCW加分层调制可接近MCW。 [抽取文本，L131](../sources/NR_AH_1701/Docs/R1-1700795.txt#L131) · [3GPP官方文件](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_AH/NR_AH_1701/Docs/R1-1700795.zip)

> there is about 7~8dB gain of using SCW with per-layer modulation

### E068 — R1-1703341

作者主张2CW以改善每层LA。 [抽取文本，L61](../sources/TSGR1_88/Docs/R1-1703341.txt#L61) · [3GPP官方文件](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_88/Docs/R1-1703341.zip)

> 2 codewords can achieve up to 28%, 32% and 20% of gain

### E069 — R1-1709231

优先流水线及空间分集，灵活对应须再用SLS证明。 [抽取文本，L157](../sources/TSGR1_89/Docs/R1-1709231.txt#L157) · [3GPP官方文件](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_89/Docs/R1-1709231.zip)

> Link-level evaluation results on layer mapping schemes

### E070 — R1-1710426

UE推荐CW内层分组。 [抽取文本，L174](../sources/NR_AH_1706/Docs/R1-1710426.txt#L174) · [3GPP官方文件](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_AH/NR_AH_1706/Docs/R1-1710426.zip)

> around 18 % for SNR = 20 dB and 15 % at SNR = 25 dB

### E071 — R1-1710517

收益与信道及CB数有关。 [抽取文本，L121](../sources/NR_AH_1706/Docs/R1-1710517.txt#L121) · [3GPP官方文件](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_AH/NR_AH_1706/Docs/R1-1710517.zip)

> The gain is dependent on the channel

### E072 — R1-1710175

按layer-set集中CBG有利于不均匀干扰及独立重传。 [抽取文本，L71](../sources/NR_AH_1706/Docs/R1-1710175.txt#L71) · [3GPP官方文件](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_AH/NR_AH_1706/Docs/R1-1710175.zip)

> more than 10% gain is achieved for cell-edge UE

### E073 — R1-1711606

按layer-set集中CBG有利于不均匀干扰及独立重传。 [抽取文本，L71](../sources/NR_AH_1706/Docs/R1-1711606.txt#L71) · [3GPP官方文件](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_AH/NR_AH_1706/Docs/R1-1711606.zip)

> more than 10% gain is achieved for cell-edge UE

### E074 — R1-1710594

联合交织均衡同CBG中各CB受损程度。 [抽取文本，L106](../sources/NR_AH_1706/Docs/R1-1710594.txt#L106) · [3GPP官方文件](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_AH/NR_AH_1706/Docs/R1-1710594.zip)

> joint frequency-time interleaver

### E075 — R1-1710611

延迟宽松的高速应用受益于时间分集。 [抽取文本，L67](../sources/NR_AH_1706/Docs/R1-1710611.txt#L67) · [3GPP官方文件](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_AH/NR_AH_1706/Docs/R1-1710611.zip)

> Multi-OFDM symbol interleaver can further improve BLER performance for high Doppler scenario.

### E076 — R1-1711152

多个CB/symbol时可获多dB增益。 [抽取文本，L144](../sources/NR_AH_1706/Docs/R1-1711152.txt#L144) · [3GPP官方文件](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_AH/NR_AH_1706/Docs/R1-1711152.zip)

> dB gains for achieving TBLER=10%

### E077 — R1-1709904

倾向FLT，指出SIC高时延复杂度。 [抽取文本，L81](../sources/NR_AH_1706/Docs/R1-1709904.txt#L81) · [3GPP官方文件](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_AH/NR_AH_1706/Docs/R1-1709904.zip)

> Evaluation Results

### E078 — R1-1712703

UE推荐CW内层分组。 [抽取文本，L174](../sources/TSGR1_90/Docs/R1-1712703.txt#L174) · [3GPP官方文件](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_90/Docs/R1-1712703.zip)

> around 18 % for SNR = 20 dB and 15 % at SNR = 25 dB

### E079 — R1-1715430

时间分集收益与hop/DMRS配置耦合。 [抽取文本，L85](../sources/NR_AH_1709/Docs/R1-1715430.txt#L85) · [3GPP官方文件](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_AH/NR_AH_1709/Docs/R1-1715430.zip)

> up to 41% gain can be achieved in scheme 2-1 comparing with scheme 1-1

### E080 — R1-1716208

Option3在分集、时延和buffer间折中。 [抽取文本，L61](../sources/NR_AH_1709/Docs/R1-1716208.txt#L61) · [3GPP官方文件](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_AH/NR_AH_1709/Docs/R1-1716208.zip)

> Option-1 has around 1-2dB loss at target BLER 10%

### E081 — R1-1716284

承认多CB收益，但认为覆盖主场景低阶QAM小带宽多为1CB。 [抽取文本，L78](../sources/NR_AH_1709/Docs/R1-1716284.txt#L78) · [3GPP官方文件](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_AH/NR_AH_1709/Docs/R1-1716284.zip)

> provides ~1.3-1.8dB gain

### E082 — R1-1716387

收益取决于hop是否重叠和CB数。 [抽取文本，L61](../sources/NR_AH_1709/Docs/R1-1716387.txt#L61) · [3GPP官方文件](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_AH/NR_AH_1709/Docs/R1-1716387.zip)

> Option 3

### E083 — R1-1717295

作者不支持因低速/覆盖主场景而排除多CB收益。 [抽取文本，L67](../sources/TSGR1_90b/Docs/R1-1717295.txt#L67) · [3GPP官方文件](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_90b/Docs/R1-1717295.zip)

> Option-3 is better performance than Option-1

### E084 — R1-1720656

收益取决于hop是否重叠和CB数。 [抽取文本，L99](../sources/TSGR1_91/Docs/R1-1720656.txt#L99) · [3GPP官方文件](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_91/Docs/R1-1720656.zip)

> some loss after 5 dB of geometry may be expected

### E085 — R1-1705952

多panel不必然要求多CW，作者支持rank3/4单CW。 [抽取文本，L116](../sources/TSGR1_88b/Docs/R1-1705952.txt#L116) · [3GPP官方文件](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_88b/Docs/R1-1705952.zip)

> there is a slight degradation in leveraging two or four codewords

### E086 — R1-1702597

大分配、多CB时增加频率分集。 [抽取文本，L33](../sources/TSGR1_88/Docs/R1-1702597.txt#L33) · [3GPP官方文件](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_88/Docs/R1-1702597.zip)

> significant gains

### E087 — R1-1716723

主张时间先以获取完整时间/跳频分集。 [抽取文本，L170](../sources/NR_AH_1709/Docs/R1-1716723.txt#L170) · [3GPP官方文件](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_AH/NR_AH_1709/Docs/R1-1716723.zip)

> option 2 shows about 1.6 dB gain over option 1

### E088 — R1-1713765

高速支持时分集；纯频交织收益小。 [抽取文本，L79](../sources/TSGR1_90/Docs/R1-1713765.txt#L79) · [3GPP官方文件](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_90/Docs/R1-1713765.zip)

> Mapping order-2 shows more than 2.4 dB gain

### E089 — R1-1701071

多CW只在部分mean指标有益，edge并不一致。 [抽取文本，L81](../sources/NR_AH_1701/Docs/R1-1701071.txt#L81) · [3GPP官方文件](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_AH/NR_AH_1701/Docs/R1-1701071.zip)

> there are not gains in cell edge

### E090 — R1-1708641

多个CB/symbol时可获多dB增益。 [抽取文本，L92](../sources/TSGR1_89/Docs/R1-1708641.txt#L92) · [3GPP官方文件](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_89/Docs/R1-1708641.zip)

> dB gains for achieving TBLER=10%

### E091 — R1-1709200

多个CB/symbol时可获多dB增益。 [抽取文本，L92](../sources/TSGR1_89/Docs/R1-1709200.txt#L92) · [3GPP官方文件](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_89/Docs/R1-1709200.zip)

> dB gains for achieving TBLER=10%

### E092 — R1-1709193

CLI干扰集中时分组CBG比把误差扩散到全CB更稳健。 [抽取文本，L232](../sources/TSGR1_89/Docs/R1-1709193.txt#L232) · [3GPP官方文件](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_89/Docs/R1-1709193.zip)

> The difference in SNR to achieve the same spectrum efficiency can be several dBs.

### E093 — R1-1713688

CLI干扰集中时分组CBG比把误差扩散到全CB更稳健。 [抽取文本，L373](../sources/TSGR1_90/Docs/R1-1713688.txt#L373) · [3GPP官方文件](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_90/Docs/R1-1713688.zip)

> The difference in SNR to achieve the same spectrum efficiency can be several dBs.
