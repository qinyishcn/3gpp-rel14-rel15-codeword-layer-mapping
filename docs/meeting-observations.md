# 会议决策链与最终 observation

Meeting outcome 与提案作者 observation 分开记录。下面按Final Minutes原文确认，不以TDoc状态代替技术结论。

## O01 TSGR1_86b — §8.1.4.2 Multi-antenna scheme

启动CW-to-layer/CW数量研究，明确考虑高级接收机。

> This RAN1 study should consider advanced receivers for interference mitigation

R1-1611064；2016年Rel-14时间窗口内的NR study，不是LTE R14新规范已采纳。

[Final_Minutes_report_RAN1#86b_v100.zip, Final, Meeting outcome](../sources/TSGR1_86b/Report/Final_Minutes_report_RAN1%2386b_v100.zip) · [文本L8725](../sources/TSGR1_86b/Report/Final_Minutes_report_RAN1%2386b_v100.txt#L8725)

## O02 TSGR1_87 — §7.1.3.1 Multi-antenna scheme

1–2层1/2CW待定；3–8层1/2/≥3CW待定，要求兼顾NC-JT、控制开销和分层调制。

> Study possible use of different modulations in single codeword

R1-1613109；所有候选都是FFS。

[Final_Minutes_report_RAN1#87_v100.zip, Final, Meeting outcome](../sources/TSGR1_87/Report/Final_Minutes_report_RAN1%2387_v100.zip) · [文本L7874](../sources/TSGR1_87/Report/Final_Minutes_report_RAN1%2387_v100.txt#L7874)

## O03 TSGR1_88 — §8.1.2.1.1 Codeword mapping, pp74–75

1–2层1CW、5–8层2CW成为agreement；3–4层1CW仍是working assumption。

> For 1 to 2-layer transmission: 1 codeword

早先Possible agreement/objections不是最终agreement；参考R1-1703967/3989/4012。

[Final_Minutes_report_RAN1#88_v100.zip, Final, Meeting outcome](../sources/TSGR1_88/Report/Final_Minutes_report_RAN1%2388_v100.zip) · [文本L6311](../sources/TSGR1_88/Report/Final_Minutes_report_RAN1%2388_v100.txt#L6311)

## O04 TSGR1_88b — §8.1.2.1.1 Codeword mapping, pp74–75

3–4层1CW被确认为agreement；额外2CW仍FFS；每CW一个MCS和CQI。

> For 3 and 4-layer transmission, NR supports 1 codeword (CW) per PDSCH/PUSCH assignment per UE

R1-1706215；同CW的DMRS端口组可以具有不同QCL。

[Final_Minutes_report_RAN1#88b_v100.zip, Final, Meeting outcome](../sources/TSGR1_88b/Report/Final_Minutes_report_RAN1%2388b_v100.zip) · [文本L6074](../sources/TSGR1_88b/Report/Final_Minutes_report_RAN1%2388b_v100.txt#L6074)

## O05 TSGR1_89 — §7.1.2.1.1 Codeword mapping, p83

>4层每CW最多4层，基准为接近平分；LFT仅为working assumption，其他方案仍研究。

> For >4-layer transmission, each of the two CWs is mapped to at most 4 layers

R1-1709261/9356/9360；公式必须看原Word/保留OMML，不能将文本EQ占位符当公式。

[Final_Minutes_report_RAN1#89_v100.zip, Final, Meeting outcome](../sources/TSGR1_89/Report/Final_Minutes_report_RAN1%2389_v100.zip) · [文本L6945](../sources/TSGR1_89/Report/Final_Minutes_report_RAN1%2389_v100.txt#L6945)

## O06 NR_AH_1706 — §5.1.2.1.1 Codeword mapping, p32

补充公平评估要求：URLLC、hopping、dynamic TDD、HST、CBG-HARQ、PI、DMRS、slot/mini-slot。

> Practical simulation assumptions e.g. CBG based HARQ, pre-emption indication, DMRS, interleaver should be considered.

R1-1711935；本会未终结额外映射和交织争议。

[Final_Minutes_report_RAN1#AH_NR2_v100.zip, Final, Meeting outcome](../sources/NR_AH_1706/Report/Final_Minutes_report_RAN1%23AH_NR2_v100.zip) · [文本L2500](../sources/NR_AH_1706/Report/Final_Minutes_report_RAN1%23AH_NR2_v100.txt#L2500)

## O07 TSGR1_90 — §6.1.2.1.1 Remaining details on codeword mapping, p81

Rel-15 DL和CP-OFDM UL只支持L→F→T；无额外频率/时间交织；DFT-s仍FFS。

> No frequency and/or time interleaving is supported in Rel-15 NR

R1-1714664；这里的interleaving是本议题的额外CW/CB资源交织，不能说NR不存在编码内交织或VRB-to-PRB interleaving。

[Final_Minutes_report_RAN1#90_v100.zip, Final, Meeting outcome](../sources/TSGR1_90/Report/Final_Minutes_report_RAN1%2390_v100.zip) · [文本L6655](../sources/TSGR1_90/Report/Final_Minutes_report_RAN1%2390_v100.txt#L6655)

## O08 NR_AH_1709 — §6.2.1.1 Remaining details on codeword mapping, p29

DFT-s无FH采用Option1；有FH在Option1和3间继续下选。

> For RE mapping for DFT-S-OFDM without frequency hopping:

R1-1716858；不再保留Option2作为本轮下选候选。

[Final_Minutes_report_RAN1#AH_NR3_v100.zip, Final, Meeting outcome](../sources/NR_AH_1709/Report/Final_Minutes_report_RAN1%23AH_NR3_v100.zip) · [文本L2280](../sources/NR_AH_1709/Report/Final_Minutes_report_RAN1%23AH_NR3_v100.txt#L2280)

## O09 TSGR1_90b — §7.2.1.1 Remaining details on codeword mapping, p80

Rel-15 >4层不增加CW-layer correspondence；2/3/4层额外2CW在2017年12月完成范围内无共识。

> No additional CW-layer correspondence is supported, at least in Rel-15, for >4 layers

R1-1718798源ZIP损坏，以正式Final Minutes中的原句为证；不是“灵活映射没有任何仿真收益”。

[Final_Minutes_report_RAN1#90b_v100.zip, Final, Meeting outcome](../sources/TSGR1_90b/Report/Final_Minutes_report_RAN1%2390b_v100.zip) · [文本L6295](../sources/TSGR1_90b/Report/Final_Minutes_report_RAN1%2390b_v100.txt#L6295)

## O10 TSGR1_90b — §7.2.1.1, p80

单CB的DFT-s intra-slot FH采用Option1为working assumption，多CB仍FFS。

> For DFT-SOFDM for single codeblock with intra-slot frequency hopping, only Option 1 is supported:

R1-1718991修订为1719137；不能提前称多CB已结论。

[Final_Minutes_report_RAN1#90b_v100.zip, Final, Meeting outcome](../sources/TSGR1_90b/Report/Final_Minutes_report_RAN1%2390b_v100.zip) · [文本L6307](../sources/TSGR1_90b/Report/Final_Minutes_report_RAN1%2390b_v100.txt#L6307)

## O11 TSGR1_91 — §7.2.1.1 Remaining details on codeword mapping, p91

确认Option1，并扩展到多CB：先子载波、再sub-slot内symbol、最后不同PRB sub-slot。

> Confirm the working assumption and DFT-SOFDM for multiple code blocks with intra-slot frequency hopping follows the same design

R1-1721599；技术收益与处理时延/实现/适用主场景的折中。

[Final_Minutes_report_RAN1#91_v100.zip, Final, Meeting outcome](../sources/TSGR1_91/Report/Final_Minutes_report_RAN1%2391_v100.zip) · [文本L6556](../sources/TSGR1_91/Report/Final_Minutes_report_RAN1%2391_v100.txt#L6556)

## O12 TSGR1_92b — §7.1.2.1.1 Codeword mapping, p66

继续处理TB/CW与端口映射编辑：两TB→CW0/1，单TB→CW0。

> 1-TB: always mapped to CW0

后期主要维护细节，不能把所有CW标题文档都计为新仿真。

[Final_Minutes_report_RAN1#92b_v100.zip, Final, Meeting outcome](../sources/TSGR1_92b/Report/Final_Minutes_report_RAN1%2392b_v100.zip) · [文本L5018](../sources/TSGR1_92b/Report/Final_Minutes_report_RAN1%2392b_v100.txt#L5018)

## O13 TSGR1_93 — §7.1.2.1.1 Codeword mapping, p69

进一步澄清一TB被禁用时，启用TB映射到CW0。

> the enabled transport block is mapped to codeword 0.

R1-1806708；与前述CW数量/映射结论一致。

[Final_Minutes_report_RAN1#93_v100.zip, Final, Meeting outcome](../sources/TSGR1_93/Report/Final_Minutes_report_RAN1%2393_v100.zip) · [文本L5048](../sources/TSGR1_93/Report/Final_Minutes_report_RAN1%2393_v100.txt#L5048)

## R1-1711935 中明确写出的 observation（主持/讨论汇总，尚非最终agreement）

该文由Samsung汇总，不能将其中的“seem”“no clear majority”改成技术性能的标准结论。原文指出：

> All companies seem to agree on confirming the working assumption of LFT mapping order

> No consensus on adding another mapping order (some companies are against)

> No clear majority among different positions

[R1-1711935, Summary of Open Issues on Layer Mapping, Proposal / rapporteur summary, NR AH2, §Mapping order / Frequency interleaving](../sources/NR_AH_1706/Docs/R1-1711935.zip)

它说明当时争议在“LFT以外是否增加方案、是否交织及如何交织”，并非所有公司仿真得出同一个增益。最终以#90、#90bis、#91正式记录及TS 38.211 V15.2.0为准。