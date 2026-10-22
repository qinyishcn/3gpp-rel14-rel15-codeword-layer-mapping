# CW-to-layer mapping 仿真与标准化观察

分析日期：2026-10-22。范围：RAN1 #80–#94bis的23次常规/bis会议，加2017年1/6/9月及2018年1月4次NR Ad-hoc，共27次。此处“Rel-14/15阶段”包含NR study与制定期，不将会议日期直接当成功能Release。

## 先分清比较了什么

| 决策轴 | 方案举例 | 合适的基线 | 最容易混淆的收益 |
|---|---|---|---|
| CW数量 | 一个CW跨多层；双CW；每层一个CW | 同rank/同receiver/同CSI的另一CW数量 | 把CW-SIC与MMSE更换的收益全归给CW数 |
| CW与空间层的对应 | 固定平分；按层质量动态分组；不同层数分割 | 相同2CW下的固定映射 | 把12%动态分组收益当成增加CW数量收益 |
| CW/CB到RE的顺序 | LFT、LTF、FLT、layer-set/CBG映射 | 相同CW数下的另一映射顺序 | 把单层高速LTF收益当高秩CW分组收益 |
| 额外交织/跳频映射 | per-symbol频交织、跨symbol时频交织、跨hop Option3 | 无交织、仅频交织或hopping Option1 | 把CBGER目标的dB差当系统吞吐百分比 |

L=layer，F=frequency，T=time；SLS=system-level simulation；LLS=link-level simulation；UPT=user-perceived throughput；CBGER=code block group error rate。单CW内“不同层使用不同QAM”与不同CW各自使用不同MCS是两种方案。

## CW数量：相反结果都有原文

ZTE在R1-1701790 Tables1–3报告，单TRP的rank2双CW对单CW在UMi SU的mean UPT提高3.72～13.33%，5%-UPT提高19.42～55.14%；MU平均SE提高2.96%，5%-SE提高31.90%。Indoor、UMi、不同负载不能并成一个统一数值。它强调逐层LA、干扰和独立重传。其NCJT与DPS/DPB比较另有更大收益，但DPS/DPB基线已经使用双CW，因此不能说那是双CW相对单CW的收益。[R1-1701790, “On number of codewords for NR”, Proposal, RAN1#88, §Performance evaluation](../sources/TSGR1_88/Docs/R1-1701790.zip)。

Huawei/HiSilicon在R1-1705073 Figure1的固定rank4、8T8R测试中，双CW对单CW的mean为+15.04/+17.00/+17.47%，5%-UPT为+57.33/+68.65/+51.23%，对应λ1.2/2.4/5.2。中位数图值为+25.23/+35.20/+42.32%；正文“最高43.2%”与图不一致，本报告采用原图42.32%。这些最大值不是同一个负载下同时达到。[R1-1705073, “Codeword to layer mapping in NR”, Proposal, RAN1#88bis, §Discussion on codeword number/Figure1](../sources/TSGR1_88b/Docs/R1-1705073.zip)。

Intel在R1-1702187 Table1的UMa、2Rx、MMSE-IRC、FTP/PF/OLLA条件中，单CW对双CW的mean提高4～7%、5%-UPT提高5～10%。到rank3/4，R1-1704717的EMF内嵌表给出单CW/双CW的mean分别70.19/69.83、66.72/66.28、63.50/63.03Mbps，作者均取整标成约+1%；负载很低，RU约4.1～8.6%。[R1-1702187, Proposal, #88, §SU-MIMO/Table1](../sources/TSGR1_88/Docs/R1-1702187.zip)；[R1-1704717, Proposal, #88bis, §SU-MIMO performance for rank3 and4/Table1](../sources/TSGR1_88b/Docs/R1-1704717.zip)。

Ericsson在R1-1705883 Tables1–4对rank3/4给出的双CW normalized UPT相对单CW是+1/+4/+3/-2%，edge为-1/+4/+4/-3%；判断二者相近。Samsung在R1-1702916各表中，双CW平均UPT为单CW的94.9～98.4%，同样未看到引入双CW的普遍收益。它们把单CW的优势联系到分集、CSI误差平均化和LA稳健性。[R1-1705883, Proposal, #88bis, §On the number of codewords](../sources/TSGR1_88b/Docs/R1-1705883.zip)；[R1-1702916, Proposal, #88, Tables1–3](../sources/TSGR1_88/Docs/R1-1702916.zip)。

Nokia/ASB又提供一个有意义的反例：30GHz、TRP/UE各4sub-panels、8RF beam ports、wideband eigenbeamforming的相干多panel SLS中，最多2或4CW比单CW略差。因此“存在多panel”本身不足以推出“必须多CW”；是否相干、层间SINR、CSI和LA都影响比较。[R1-1705952, Proposal, #88bis, §System-level simulation/Figure4](../sources/TSGR1_88b/Docs/R1-1705952.zip)。

**Derived analysis**：这些文档证明了场景依赖和trade-off，没有提供一个跨公司可直接平均的共同增益。尤其不能把mean、5%-UPT、sector throughput、SE、BLER目标dB混合统计。

## 真正的灵活空间层分组收益

AT&T的R1-1702262固定rank4、2CW，动态选择{12|34,13|24,14|23}，对固定{12|34}报告约12% SE收益。R1-1707737进一步给出rank8在20/25dB约18%/15%的LLS收益，以及3DUMa、2GHz/5MHz、57TRPs、fullbuffer、MMSE-IRC的SLS约11% average sector throughput和10%“90% throughput”收益。这里比较保持2CW，属于空间层分组变化。[R1-1702262, Proposal, #88, Figures1–2](../sources/TSGR1_88/Docs/R1-1702262.zip)；[R1-1707737, Proposal, #89, §Dynamic layer mapping/§System Level Simulation Results](../sources/TSGR1_89/Docs/R1-1707737.zip)。

需要注意，AT&T LLS采用ideal CE、零控制开销、误差为零的4TTI反馈等条件；其所称最弱层控制CQI也是作者的具体LA设定，不能当成所有接收机的必然行为。增加映射选择还涉及反馈、DCI、layer ordering、可实现的CSI精度和最终规范复杂度。最终#90bis不增加额外correspondence，是采用范围的决定，不是对上述提案图中收益的否认。

## 资源顺序、交织和hopping：另外三组收益

Qualcomm的单CW内分层QAM相对统一QAM，在特定30GHz双panel例子报告rank2约1.5dB、rank4约7～8dB；它在另一些sub6例子接近多CW性能。R1-1705574中的约7% mean SE“系统收益”是用LLS曲线与几何CDF组合推估，不是独立动态SLS。[R1-1702596, Proposal, #88, §Performance evaluation/Figures8–9](../sources/TSGR1_88/Docs/R1-1702596.zip)；[R1-1705574, Proposal, #88bis, §Performance results](../sources/TSGR1_88b/Docs/R1-1705574.zip)。

频域inter-CB交织也没有固定增益。Qualcomm在LDPC 8192bits、4层、SCW、64/256QAM8/9、45～275PRB条件中，10%TBLER的收益约0.1～>5dB；大值来自特定高MCS、大带宽、多CB/symbol场景。Intel的64QAM、约2.9～3.5CB/symbol测试则为0.3～0.84dB；Huawei一些3km/h配置≤0.4dB，AT&T某些自适应配置只约2%高SNR吞吐收益。不能由一个定MCS误码曲线代表所有动态LA系统。[R1-1708579, Proposal, #89, §Performance Evaluations/LDPC table](../sources/TSGR1_89/Docs/R1-1708579.zip)；[R1-1712536, Proposal, #90, Table3](../sources/TSGR1_90/Docs/R1-1712536.zip)；[R1-1708128, Proposal, #89, Figure2](../sources/TSGR1_89/Docs/R1-1708128.zip)；[R1-1707737, Proposal, #89, Figures6–9](../sources/TSGR1_89/Docs/R1-1707737.zip)。

高速时域分集是Huawei/HiSilicon、ETRI等的重要论据。R1-1712228 TableI对LTF相对LFT在60km/h为1.6～2.0dB、120km/h为2.3～3.4dB、350km/h为3.3/4.5dB，目标BLER10%；各MCS、rank、delay spread和DMRS不同。Lenovo/Motorola在URLLC穿孔下以CBGER10%比较，AWGN文R1-1710594为联合时频交织相对仅频交织0.9～2.1dB，后续CDL-A/SFBC文R1-1712670为0.31～3.1dB，两文不能复制同一范围。[R1-1712228, Proposal, #90, TableI](../sources/TSGR1_90/Docs/R1-1712228.zip)；[R1-1710594, Proposal, NR AH2, Tables2–3](../sources/NR_AH_1706/Docs/R1-1710594.zip)；[R1-1712670, Proposal, #90, Table1](../sources/TSGR1_90/Docs/R1-1712670.zip)。

DFT-s-OFDM跳频又是单层UL的RE映射问题。NTT DOCOMO、Intel、MediaTek等在多CB时看到Option3相对Option1约1～2dB量级优势；单CB通常相同。争议涉及首CB可多早开始解码、UE Tx buffer、非对称hop、MPR和覆盖边缘主场景的低MCS/窄带配置，最终#91采用Option1。详见证据表E052–E059等及正式会议结论；不把这些数字放进“灵活CW空间分组”一栏。

## 最终 observation：技术综合与正式决定分别说

**Derived analysis**：多CW/灵活层分组能够利用层间不均匀质量并支持独立LA、HARQ或CW级IC；单CW能提供跨层分集、减小反馈/控制字段并利于流水线。时间/频率分集可以改善特殊信道、干扰或穿孔条件，但要结合CBG、PI、DMRS、rank/LA和处理时延评估。仿真条件差异导致正负结果并存。

**Proposal / rapporteur summary 的原文 observation**：NR AH2的R1-1711935写到各方似乎接受LFT作为共同基础，但增加其他顺序没有共识，交织路线也无清晰多数。这里是讨论状态总结，没有认可一个统一数值。[R1-1711935, “Summary of Open Issues on Layer Mapping”, §Mapping order/§Frequency interleaving](../sources/NR_AH_1706/Docs/R1-1711935.zip)。

**Meeting outcome / Normative 的最终结果**：DL 1–4层1CW、5–8层2CW；高rank按2+3、3+3、3+4、4+4固定分割。UL最多4层1CW。DL/CP-OFDM UL采用LFT；Rel-15不增加本议题的额外时频交织或>4层CW-layer correspondence；DFT-s跳频采用Option1并扩展到多CB。完整按会次的原句、文档版本、章节和本地源路径见[会议结论表](meeting-observations.md)，最终mapping由[TS38.211 V15.2.0, §6.3.1.3、§7.3.1.3/Table7.3.1.3-1, Normative](../sources/specs/38211-f20.zip)核对。

## 复用、数值和覆盖规则

93条记录涉及77份文件，不是77个独立实验。修订稿、不同会议复用曲线、SLS统计而非吞吐对照、LLS×CDF推估均在表中注明。所有英文摘录做逐字匹配，原文绝对数值和百分比方向保留。

“A比B损失20%”意味着A=0.8B，反向B比A提高25%，不是20%；此为数学说明，不是新增仿真。Samsung表的94.9%是相对单CW的比值，意味着-5.1%。达到BLER10%所需绝对SNR=14dB不等于增益14dB。NCJT与DPS的差异包含TRP协调、rank、数据流等；跨receiver比较必须保留receiver名称。

[覆盖清单](coverage.md)披露4个官方目录无文件和1个损坏ZIP，以及题名筛查可能遗漏一般MIMO/CoMP题名文档的边界。原始ZIP不删除，公式、图片、二维表在原Word中完整保留；抽取文本中的FIG/EQ为导航占位符，不能替代原图公式。
