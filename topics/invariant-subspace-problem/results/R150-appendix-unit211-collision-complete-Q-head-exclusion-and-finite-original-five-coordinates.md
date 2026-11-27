# R150：碰撞图两条原 Q 首项零纤维排除与五坐标有限性

数据保存说明（2026-11-28）：可重算载荷已按根规矩8/15从main移除，相关旧链接只定位既有历史；当前保留生成源、参数定义、run与SHA，原数学及执行身份不变。


日期：2026-11-28（Asia/Taipei）。会话：Astra-ISP-8542378f-20261127。

在当前原 $h_U=k_U$、$\Delta\ne0$ 碰撞图中，
$$
G_2(\lambda)=\lambda^2+\lambda-1,\qquad
C_4(\lambda)=8\lambda^4-24\lambda^3+24\lambda^2-12\lambda+3
$$
的整个原零纤维都已排除。于是原 $C_W$ 的 Q 六次首项在余下图上处处非零。

结合已完成的两个原 QQ 投影及整条 $J_2,P_{25,3}$ 排除，剩余不同的同点五坐标
$$
(\lambda,u,Q,f,z)
$$
至多为 **235170**。它们还容纳于维数不超过 235170 的有限 QQ 代数环境中；全原方程只会进一步取商。这个有限性结论没有证明剩余原点不存在，也不把它外推到其它权图、unit211 或普通 Hilbert ISP。

## 1. 已付的完整必要输入

[两条原 QQ 投影](R150-appendix-unit211-equal-singleton-two-original-QQ-projections-common-curves-and-finite-base-remainder.md)给出必要覆盖
$$
J_2=0\quad\hbox{或}\quad P_{25,3}=0
\quad\hbox{或}\quad E_1(\lambda,u)=E_2(\lambda,u)=0,
$$
其中 $E_1=E_{177,18}$、$E_2=E_{182,19}$，两个不同不可约因子的总次数分别为 195、201。此前[整 J2 原纤维](R150-appendix-unit211-entire-J2-complete-original-fiber-exclusion.md)和[整 P25,3 原曲线](R150-appendix-unit211-collision-P3-entire-original-exclusion.md)已经关闭。因此当前每个原点都满足同一对
$$
E_1(\lambda,u)=E_2(\lambda,u)=0. \tag{1.1}
$$

本次直接读取这两个已保存因子的全部准确系数，没有重做原 Q 投影。原始参数清单为
[2026-11-28-unit211-collision-two-QQ-projections-exact-factor-manifest-8542.json](https://github.com/Rogerhu12/math-research-public/blob/3b9cda56dfa6a1ae9d4ca2a35fa81798a5f156c9/topics/invariant-subspace-problem/notes/2026-11-28-unit211-collision-two-QQ-projections-exact-factor-manifest-8542.json)；
两个因子各两片，每片文件 SHA、拼接编码 SHA 及解压载荷 SHA 均在输入时实际检查。

同一旧原 QQ 首项分解还已给
$$
[Q^6]C_W
=\kappa\,\lambda^4 A^{13}J_2G_2^2C_4^2,\qquad
A=2\lambda^2-2\lambda+1,\quad \kappa\in\mathbb Q^\times. \tag{1.2}
$$
原首项次数为 44；剥 $\lambda^4 A^{13}$ 后的完整 14 次因子及所有重数都已实际乘回。这里不再计算这个已完成首项。当前仅剩 $G_2,C_4$ 两个未知零纤维，$\lambda,A,J_2$ 已由原域或独立原排除支付。

## 2. 两个完整常数域与原 u Bezout

本次首先在 QQ 上准确分解 $G_2,C_4$，二者分别是次数 2、4 的不可约多项式，重数一；实际因子乘积等于原输入。取整个常数域
$$
K_2=\mathbb Q[\lambda]/(G_2),\qquad
K_4=\mathbb Q[\lambda]/(C_4).
$$
没有选取一个复根或一个模素数嵌入。

在每个域中，直接专门化 (1.1) 的全部原系数。两条 u 多项式的实际次数均仍为 18、19；源码本身按实际次数去掉零首项，所以即使发生下降也不会倒置一个已经消失的首项。对这些准确多项式运行带完整系数的 u Euclid，并逐步乘回除法，最后实际核对
$$
a(u)\,E_1(\lambda,u)+b(u)\,E_2(\lambda,u)=g(u). \tag{2.1}
$$
这是真正同一个 $\lambda,u$ 的原组合，非分别选根的范数条件。

在 $K_2[u]$ 中，实际得到
$$
g(u)=1. \tag{2.2}
$$
因此 $G_2=0$ 的整个 (1.1) 纤维已空，无须再引入 Q 或原值变量。

在 $K_4[u]$ 中，准确得到
$$
g(u)=u^4-4u^3+6u^2-4u+1=(u-1)^4. \tag{2.3}
$$
所以任一满足 (1.1) 的原复点都必须有 $u=1$，与当前原图已付的 $u\ne1$ 矛盾。

这个结论也保持整个非约化纤维。实际返回将 $(u-1)^4$ 逐次分为
$$
(u-1)(u-1)^3,\quad
(u-1)(u-1)^2,\quad
(u-1)(u-1),
$$
每次原乘积都核回，两侧都保留。四条最终叶均由同一个原单位 $u-1$ 恒零排除；没有假称这些因子互素或删掉幂零结构。等价地，在当前 $u-1$ 已可逆的原域中，(2.1)–(2.3) 已给单位。

两个实际完整 Bezout 证书的规范编码分别为：

| 整常数域 | gcd | 编码字节数 | SHA256 |
|---|---|---:|---|
| $K_2$ | $1$ | 309430 | 0511446584a2dabe526bae737e06cc55fc1cdda20a50d9a85c65af6d682fb28f |
| $K_4$ | $(u-1)^4$ | 289800 | 57582f1326de03d314d02d49a3ee6bfda0bef8d808218afd03b3f92bcc8f95c9 |

完整确定性源和所有小输入可重建这些系数，因此不把大 Bezout 缓存另存为仓库副本。小回执保真实 gcd 系数、所有实际路径和证书 SHA。

本次在原 u 层已经排除两图；后备的原 Q gcd、Delta 幂及其它物理目标返回都没有执行，不能列作额外已成证书。

## 3. 原 Q 次数现在有全域控制

由第 2 节以及已付 $\lambda A J_2\ne0$，(1.2) 在当前剩余图上处处非零。因此
$$
\widehat C_W=C_W/[Q^6]C_W
$$
是真正首一的 Q 六次必要式。全部未知的原 Q 首项零图都已经独立覆盖；这里不是先丢掉首项零点再数根。

两条 (1.1) 曲线没有共同分量，平面 Bezout 给不同复仿射基点数至多
$$
195\cdot201=39195.
$$
每个基点的完整首一 Q 六次式至多有六个不同复根，所以不同同点三元组至多
$$
6\cdot39195=235170. \tag{3.1}
$$
原 $C_R,C_O,C_{N1}$ 以及全部个别 N/P 条件都还须满足；使用其中一条必要六次式取得的只是上界，不是所有候选都能提升为原点。

## 4. 同点原 f,z 恢复与有限代数环境

[四个同点原式的完整来源](R150-appendix-unit211-equal-singleton-Delta-nonzero-four-complete-original-polynomials.md)已在当前碰撞图返回原两条线性关系
$$
P_f f+bc\,\Phi z+P_c=0,\qquad
N_F f+bc\,S\xi z+N_C=0.
$$
采用该文同样的符号，
$$
\Delta=\Phi N_F-S\xi P_f,\quad
F_{\rm num}=S\xi P_c-\Phi N_C,\quad
T_{\rm num}=P_fN_C-P_cN_F.
$$
整个 $\Delta=0$ 原分支已有独立排除，且 $bc\ne0$ 是当前原域条件。因此每个同点三元组唯一恢复
$$
f=F_{\rm num}/\Delta,\qquad
z=T_{\rm num}/(bc\,\Delta). \tag{4.1}
$$
所有系数均在同一 $\lambda,u,Q$ 上评价。故 (3.1) 也界住五坐标 $(\lambda,u,Q,f,z)$，没有把不同 Q 根的两个原值拼在一起。

还可把这个有限性写成代数环境。令
$$
B_0=\mathbb Q[\lambda,u]/(E_1,E_2).
$$
两多项式无共同分量，所以 $B_0$ 是有限 QQ 代数；仿射交点的总长度由同一 Bezout 界给
$\dim_{\mathbb Q}B_0\le39195$。
在其中只对当前已付的原标量单位和刚证明非零的 $G_2,C_4$ 作局部化，得到 $B_1$。有限维代数的局部化只保留部分 Artin 分量，因而不会增加 QQ 维数。

于是
$$
B_1[Q]/(\widehat C_W)
$$
对 $B_1$ 自由秩六，QQ 维数不超过 235170。再局部化当前已付的 Q 相关物理单位及 $\Delta$，并加入其余完整原方程，只会保留分量或取商，不会增加该维数。(4.1) 给出的 f,z 是这个环境里的实际元素，不另引入自由坐标。

这里没有将 $B_0$ 或最终原方程商假定为约化，也没有把进一步取商后的代数称为对 $B_1$ 自由。235170 是同一原坐标环境的上界，不是全部剩余原点已被逐一排空的声明。

## 5. 唯一真实执行与继续范围

源：
[2026-11-28-unit211-collision-E-intersection-Q-head-entire-original-fibers-8542.py](../notes/2026-11-28-unit211-collision-E-intersection-Q-head-entire-original-fibers-8542.py)。

- Git blob：6e807252f4d2f22aaabc4bcf5109528632213675。
- SHA256：5c7711ece94f13751f861bbf5092ccc7a0942e07e1dcb8630af1088bb5ec0bae。
- run/job：46053691670 / 140690958605。
- source commit：0298b35143bc5e99acf40ef1bb452d7002df7d77。
- 内层实际：33.018841050 秒，峰值 54536 KiB，exit 0。
- 原数学终标：32.935539997 秒。
- stdout：8261 字节，SHA256 1a896205e45d83fcb897f1a26bf131e60ab85a562d37ab6641eef72fbb88929c。
- 固定限额：180 秒、4 GiB；没有更换素数、模提升或数值抽样。

真实 pull 于 2026-11-27 19:01:38.243433 UTC 由 0298b351… 前进到 fb29c7c8bfc813d583a4b6e4c0225a8fafc9fc83；两 README 的 blob 均无变化。源固定在已记 source commit，执行器如实分别记录源提交和实际规则读取提交。

[完整小回执](../notes/2026-11-28-unit211-collision-E-Q-head-complete-original-return-receipt-8542.json)保全部实际数学记录与驱动回执。此前 J2、P25,3、两原 QQ 投影与失败源均保持原登记；本次没有重放已完成的投影或 P3 门。

下一接口是这个有限五坐标环境内剩余的全部原 Q、个别 N/P 与原值条件。当前定理不删除任何尚未返回的候选，不完成整个碰撞图。
