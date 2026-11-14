# 全真实线性中心 producer 的独立只读审阅

geometry_audit（GPT-6 Astra Pro；AI-assisted），2026-11-13。

审阅对象为 computations/root_outer_full_linear_centre_source.py，SHA256 `987435e9cb25e8bb294623920a6d891f7c346d7762bd06055c1dc184e1950d3f`。审阅其固定 Laurent algebra（SHA `3eeb508e6a865ca3549bd25f2824a580a758a9f55a13a4b15bf016cc917a6bc0`）、signed geometry 的字段生成规则以及 R109 原证明。没有另跑 ODE、Arb、Node 或源求积；这份记录本身不替代该 producer 的正式完整终态。

本次未发现具体数学错误。核对了以下接口：

1. 全二十个非零中心模式均为同一归一齐次列的 phi/F 乘准确 Qout/S0，输出的 P 是 sine 幅度、K 是 cosine 幅度。其它26个线性高度为零，全部46个源输出仍保留。
2. Laurent algebra 将 sine 写为负虚数乘奇 Laurent 多项式的一半，cosine 写为偶多项式的一半。代码 Q 的负 U² 与正 P² 项符合这一归一；c2、完整 A2、S3 和所有零模先在全 Laurent 代数中形成。最后 2*coeff 恢复非零 cosine 输出。
3. 681*R_q^4/q^m 是完整余式的 paired 输出界，无需再加一个2。每个真实材料行仅在其实际 R_q<1/64 后采用 q=2,4,8,16；这是值余项的域，不把导数用的1/128门混入，也不假定旧 R109 的 q=8/16 尚未支付数据已经可用。
4. 对 trace-zero physical 状态 Y=F(P,K)，源为 (0,F*N)，W=det(phi,chi)。变参数公式在内 cut 的 Q 读出给正的 integral(chi_P*F*N dx)/W，因为 phi_Q(cut)=1；F、dx、W各一次。
5. 保存的 ap/ac 已含同一源面板 integral |phi_P or chi_P|*F dx；geometry 的四个 target 分量已经除 F*V。whole-field 组装只再乘 (1+m)e^(m/64)/|W|，没有第二个源尺度或目标 V。
6. prefix 和 suffix 从同一保存 positive dyadic 项准确求和，再移除已知 summand。目标所在当前 subpanel 在两侧都完整收费，虽可保守但安全。先对每个分量、每模在所有目标 subpanels 取 supremum，再做完整模式和，保留了所需强范数量词。
7. 真材料和 signed geometry 共同 refinement 的 x 覆盖、V、原panel编号、全部模式及SHA均核对；whole-panel enclosure乘准确dx是完整积分包围，不是采样求积。

仍需由父代理保留 producer 的实际完成门、全原胞元覆盖与输出SHA。其结论范围是固定完整 L_R 中心的真实源及 Green 响应，不是未知场球、完整切口或闭曲面证书。
