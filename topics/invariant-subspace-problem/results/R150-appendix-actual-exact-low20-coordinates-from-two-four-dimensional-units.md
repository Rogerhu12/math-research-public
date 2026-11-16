# R150：两个四阶数域单位给全部五十低交换子的实际精确坐标

作者：Astra-ISP-789f / normal_annihilator，与 /root 协作。AI-assisted：GPT-6 Astra Pro。日期：2026-11-16。

## 1. 本次完成的结论

在原固定三次数域
$$
E=\mathbb Q[d]/(3725d^3-43931504d^2+6080833024d+52565262336)
$$
上，同一原五十条低交换子和全部原来源，现在已有实际生成、精确乘回通过的 $20\times50$ 坐标矩阵 $\Lambda$。十二个参数 $y,w$ 没有取值；结果沿已付原来源映射给完整参数恒等式
$$
V_{\rm all}=V_{\mathcal I}\Lambda,\qquad
\sigma_{\rm all}=\sigma_{\mathcal I}\Lambda. \tag{1.1}
$$
所选二十个原索引始终为
~~~text
1,2,3,4,5, 11,12,13,14,15,
21,22,23,24,25, 31,32,33,34,35.
~~~

此次使用两个真实 $4\times4$ 的 $E$ 单位分解。同原 $20\times20$ 投影单位、两个四阶单位在合法 place $(127,d-100)$ 的行列式分别为
$$
64,\qquad96,\qquad69.
$$
两四阶逆的全部64个 $E$ 双向产品、最终1000个 $E$ 产品、3000个 faithful 有理坐标、1000个 place 产品，以及400个 selected identity 坐标，均已实际通过。

这补全了[原特征零低交换子二十维因子化](R150-appendix-original-characteristic-zero-low-commutators-factor-through-twenty-cubic-sources.md)中固定常数 $\Lambda$ 的实际物化与验证。该前文给出的完整55维来源恒等式和参数来源证明继续使用；本次新算的范围是补投影及精确坐标，不重称新支付完整 $55\times50$ 或十二参数展开。

## 2. 原结构、来源与补投影

令 $B=E[y_0,\ldots,y_5,w_0,\ldots,w_5]$，原十个普通单项式为
$$
\mathfrak m=(1,u_0,u_1,u_2,u_3,u_4,u_1u_4,u_2u_3,u_2u_4,u_3u_4).
$$
原十一矩方程写作
$$
G_g=q_g(u)+\ell_g(u)+c_g,\qquad 0\le g<11.
$$
采用同原十一二次消元单位 $U$、完整三次来源矩阵
$$
C:E^{55}\longrightarrow E^{35}
$$
和原 $C_*$ 列0至34。其准确原输入见[原十一矩理想十生成元](R150-appendix-original-eleven-moment-ideal-has-ten-parameter-module-generators.md)、[实际十六条三次边界来源](R150-appendix-complete-original-sixteen-cubic-border-source-certificates.md)及[完整原十生成元呈示](R150-appendix-complete-original-ten-generator-finite-critical-presentation.md)。

对低交换子 $V_{ij,k}=[N_i,N_j]e_{u_k}$，原来源的线性部分为
$$
z_{ij,k}=u_j\alpha_{ik}-u_i\alpha_{jk}
+\sum_v\rho_{ik,v}X_{j,v}-\sum_v\rho_{jk,v}X_{i,v}, \tag{2.1}
$$
其中 $\alpha_{ik}\in E^{11}$ 来自原 $U^{-1}$，四个保留二次的 $\alpha$ 为零；普通对角单项式不另加系数2。原边界 $X_{i,v}$ 只支撑 $C_*$ 的35列。

令 $R$ 提取原55来源坐标35至54。由于 $C_*$ 可逆，
$$
R|_{\ker C}:\ker C\longrightarrow E^{20}
$$
是同构，而 $RX_{i,v}=0$。故原补投影准确为
$$
(Rz_{ij,k})_{(g,\ell)}
=\delta_{\ell j}\alpha_{ik,g}-\delta_{\ell i}\alpha_{jk,g},
\quad g=7,\ldots,10,\quad \ell=0,\ldots,4. \tag{2.2}
$$
本次全部165个 $\alpha$ 索引、四保留列为零、50个原标签与所选20个标签均在源码中硬核。

完整父 UI 相位已实际重建并核原双向产品；其完整 stored/logical SHA 与原3418字节 manifest 逐字相同。恢复停在全部225个原二次来源系数通过后的事件，仍在原大 $C$ 构造之前。恢复成功没有把原被终止的 constants 阶段改称完成。

## 3. 用两四阶逆解同一个原系统

把
$$
\beta_{jk}=(\alpha_{jk,7},\ldots,\alpha_{jk,10})^T,\qquad
A_j e_k=\beta_{jk},\quad A_j:E^5\to E^4.
$$
所选20列按 $j=1,\ldots,4$、$k=0,\ldots,4$ 排列。给定原右端的五个四维块 $y_0,\ldots,y_4$，未知 $t_j\in E^5$ 满足
$$
A_0t_j=y_j,\qquad
-\sum_{j=1}^4A_jt_j=y_0. \tag{3.1}
$$
程序从原 $RZ_{\mathcal I}$ 取出这些块，并逐400槽验证(3.1)准确重构整个原选块。

实际 $A_0$ 取原列 $[0,1,2,3]$ 为四阶单位 $M$，余列为4。令 $L$ 在这四个行位置放 $M^{-1}$，余行为零；定义
$$
\eta_4=1,\qquad
\eta_{[0,1,2,3]}=-M^{-1}A_0e_4.
$$
全部16坐标的 $A_0L=I_4$、4坐标的 $A_0\eta=0$ 及规范自由坐标1，都已实际通过。

定义第二原方块
$$
B_4=[A_1\eta,A_2\eta,A_3\eta,A_4\eta].
$$
原20单位保证它可逆：若 $B_4\lambda=0$，取 $t_j=\lambda_j\eta$ 就得到原20单位的核。于是
$$
\lambda=-B_4^{-1}\left(y_0+\sum_{j=1}^4A_jLy_j\right),\qquad
t_j=Ly_j+\lambda_j\eta. \tag{3.2}
$$
本次还实际检查两个原四阶 place 子式非零。每个 $E$ 逆以基 $(1,d,d^2)$ 的 faithful 正则表示化为有理12行系统，先保存候选，再独立核左右两侧全部 $E$ 与 place 产品。所有实际 $\Lambda$ 系数由(3.2)的真 $E$ 运算得到，不是把模127系数提升。

## 4. 全部精确产品与来源身份

将50个原 RHS 全部按(3.2)求出，得到 $\Lambda\in E^{20\times50}$。最终独立验证
$$
(RZ_{\mathcal I})\Lambda=RZ,\qquad
\Lambda_{[:,\mathcal I]}=I_{20}. \tag{4.1}
$$
第一式逐全部1000个 $E$ 坐标进行 faithful 有理乘回；共3000个有理坐标。第二式逐全部400个精确 $E$ 坐标进行检查。还独立核第一式全部1000个 place 产品。

既有原来源定理给 $CZ=0$，且 $R|_{\ker C}$ 单射，故(4.1)严格推出
$$
Z=Z_{\mathcal I}\Lambda. \tag{4.2}
$$
对 $z\in\ker C$，原完整来源为
$$
\sigma_G(z)=z-U^{-1}\operatorname{elim}\!\left(\sum_gz_g\ell_g\right).
$$
其像是十个保留单项式中的向量 $\Phi(z)$。被消去的十一二次系数与原 $U$ 单位保证这条来源唯一；$\Phi,\sigma_G$ 均对 $E$ 线性。因此(4.2)同时给(1.1)的参数向量和原十一来源等式。通过已付固定可逆来源变换，等式运输到全部原十七梯度来源。

本结论全在原 $E$ 中成立，并保留 $y,w$ 的全部参数；只有固定数域常数逆，没有参数分母。有限域在这里用于同原单位选择与约化核验，精确 $E$ 产品单独完成。

## 5. 实际执行与准确时间

实际作业：
[run43911869940](https://github.com/Rogerhu12/math-research-public/actions/runs/43911869940)，job133455626806。新步为 original-low20-two-four-exact-final180，执行源码提交
~~~text
61e488e7f13f52b373dd6f5242434ba30924296f
~~~
该步实际退出0。数学程序记录20.893022871000085秒；observer实际21.502612865999936秒；外层21.667365357000108秒。开始/结束为2026-11-16 17:07:41.198614 /17:08:02.701422 UTC；child peak RSS151720KiB。完整数学 raw 为4064字节：
~~~text
9121290f0c2a0b4a9382e1a1caec7418de062158c93650c9012a943a34e5ca85
~~~
新数学 binding 为
~~~text
74e1caf83ffa4086c999bf8df112330b3821eb84e43d4026ed1789c37414c39f
~~~

仓库执行身份：
[43911869940-original-low20-two-four-exact-final180.json](../notes/r150-original-exact-low20-execution-789f/43911869940-original-low20-two-four-exact-final180.json)。
原数学字段及最后小证明相位在完成 job 日志中；后者在写日志前另核 stored/logical 双 SHA。

同作业旧 rational60 final300 确被 observer 的360秒外层期限终止，child−15/shell143。这个旧失败保留，整个 job 因而显示 failure；最后六步的 missing=[]，失败列表只含旧 rational60。新两四阶步骤的成功不改写旧身份，也不从旧未返回的求解宣称得到候选。

## 6. 可重现源码与完整相位身份

主源为
[2026-11-16-r150-original-low20-two-four-exact-789f.py](../notes/2026-11-16-r150-original-low20-two-four-exact-789f.py)，19739字节，SHA
~~~text
94033eafe24b5e5882c44ccb13be4021dafcb00d3cfea558915f8f236799164d
~~~
完整参数见[inputs](../notes/2026-11-16-r150-original-low20-two-four-exact-inputs-789f.json)，数学范围与原 argv 见[interface](../notes/2026-11-16-r150-original-low20-two-four-exact-interface-789f.md)。固定 Python3.12.14、python-flint0.9.0；执行前实际编译冻结源码。

完整新 manifest 为5528字节，SHA
~~~text
c446a7f751c9ce2907ee79133191abec47597cb8395b4d828fe8ff1029866885
~~~

核心临时相位身份：

| 相位 | stored bytes / SHA256 | logical bytes / SHA256 |
|---|---|---|
| 原投影20×50 | 4220436 / 2047435cbe8261388be61a52fef525ba9cd067d6ca10229d49558c9a7483e262 | 8553158 / 3a8ec574fc2e6a68578fef08be69375369800a2916899bda738e651240f6b333 |
| 两四阶完整分解 | 2113705 / c8f344ffe34e8ac0e780549329fd1daf5092b8f2c74e59ae8a11a865c35cee8a | 4250285 / 0baca1e5b7d20474ecff8b298172a4ae150befdbe339066d7f3c65ba0c99d048 |
| 实际坐标候选，后经最终全乘回 | 29481191 / 0ee7a67236274c9b11fe39745154d2af7ef1eb8f2fb84b67cb4c84ac5d770f45 | 59272706 / afb1ddd61050a4ad04e35c0fe66bcc6ddcb1542402b41dc9edf6d691e36210b0 |
| 完整乘回小证明相位 | 1268 / a227cb1d5fb53e998a6d2fd5a9c153f46cb2d35eb9e083269ebcf7a9fd9ab5a6 | 2484 / 2354e4e3df4285d7fc0b7d187a33c9512c2a2fcef3780e6f64520cd456894539 |

其余四相位是两个逆各自的候选与已验证逆，完整描述符均在实际回执中。候选相位名保持 candidate，证明地位由最后完整乘回相位支付，不靠改名。所有数学数组仅临时保存；本文和执行身份保源、参数、run 与 SHA。

## 7. 对参数模的立即推论及范围

原100个交换子分成十个字面零、50个低和40个高。由本次同原精确坐标，
$$
B\langle6Y,100C,10\mathrm{Bell}\rangle
=
B\langle6Y,20C_{\rm low},40C_{\rm high},10\mathrm{Bell}\rangle.
$$
这是普通 $B$ 子模等式。结合[原数域至多两轮定理](R150-appendix-original-characteristic-zero-two-round-closure-and-finite-parameter-presentation.md)，仍给至多
$$
66(1+5+4)+10=670
$$
条命名列的完整原参数呈示。这里不宣称这些列独立，不宣称原商为零。

四十高交换子的进一步吸收需要独立四次来源核证明；本篇不从低20坐标直接删除高列。原 Bell 非零分支判空与 ISP 总问题不由本次常数坐标结论解决。

## 8. 根独立完成日志与原字典审计

root 全文审上述主源、输入、接口和本稿后，另实际运行[纯 JavaScript 审计源](../notes/2026-11-16-r150-exact-low20-quartic95-completed-job-log-audit-789f.js)；其[执行身份](../notes/2026-11-16-r150-exact-low20-quartic95-root-log-audit-execution-789f.json)保全部输入与输出哈希。原完成日志为126498字节，SHA 2ff14891c18584904e659b581baa874bbea508ac4670b2ce0d3074c8d5128065。

审计从普通单项式、全部50标签、20所选列和原55来源位置重新生成完整字典，独立重建两四阶输入 semantic，得到同一原 binding。它从日志无损重建4064字节实际 raw 及2484字节最终小证明相位，全部 SHA 与原回执精确相同；原20行列式还满足同一有序块的 $96^4\cdot69\equiv64\pmod{127}$。

这项审计核的是冻结源码、完整实际门、原绑定及完整回执字节，没有重跑大有理算术，也没有从哈希恢复大系数数组。高95的独立实际回执同时核同，但其原数域来源推论另文处理。
