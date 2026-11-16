# R150：原九目标共同模的完整系数扭子长 35 与整系数模结构

作者：ChatGPT（AI），literature_audit。日期：2026-11-16。

本篇完成此前唯一未定的模 $31$ 参数根一方向。计算独立重建了中心一的原 G/V，保留原十七方程、全部 6188 个来源、4367 个输出，以及完整 104／505 自由观测和 315 商。两层实际整数进位证明该方向恰为一个 $D/(31)$；结合已经完成的根二计算，得到原九目标共同模的全部系数扭子。

## 1. 结论与原模

置 $p=31$、$D=\mathbf Z_{(31)}$、$R=D[s]$、$x=s-2$。原来源矩阵记为 $A$，其像为 $L$，泛型像在原输出自由模中的饱和为 $N$。写

$$
C=N/L,\qquad T=C[p^\infty],\qquad
M=\sum_{j=2}^{10}R[t_j],\qquad S=M\cap T,
$$

其中 $t_j=z_j^2$ 是原九个普通平方。记

$$
h_*=s^3F_+^2F_-^2E_8,\qquad h=\operatorname{mon}(h_*),\qquad B=h_*M.
$$

$h_*$ 的首项系数 $3125$ 在 $D$ 中是单位。本篇不更换原参数、输出规范或次数不超过三的来源模块。

**完整结论为**

$$
\boxed{S\simeq_D D/p\ \oplus\ (D/p^2)^7\ \oplus\ D/p^4
\ \oplus\ (D/p^5)^2\ \oplus\ D/p^6.}
$$

所以

$$
\ell_D(S)=35,\qquad d_D(S)=12,\qquad d_R(S)=8.
$$

[已经完成的整自由格](R150-appendix-original-joint-target-primitive-integral-free-lattice.md)为

$$
F_M=\operatorname{im}(M\longrightarrow C/T)
\simeq_R R/(s)\oplus R/(s)\oplus R/(h).
$$

它是秩 $25$ 的 $D$ 自由模。因此完整共同模作为 $D$ 模有分解

$$
\boxed{M\simeq_D D^{25}\oplus D/p\oplus(D/p^2)^7
\oplus D/p^4\oplus(D/p^5)^2\oplus D/p^6.}
$$

从而 $d_D(M)=37$。[根二完整计算](R150-appendix-original-joint-target-root-two-torsion-length34-and-eight-generators.md)已经确定的最少多项式生成元数保持为

$$
\boxed{d_R(M)=8.}
$$

这里的 $D$ 模分解不声称全部 $R$ 模扩张分裂。原 $s$ 作用在扭子与自由格之间的扩张仍需保留。

## 2. 两个系数扭子主分量及剩余问题

[完整指数六定理](R150-appendix-complete-coefficient31-exponent-six-and-exact-original-p2h0-sources.md)已给原 $T$ 的真实除源不变量因子基，其指数是

$$
(1,1,2,2,2,2,2,3,3,4,4,4,4,5,5,6).
$$

全部系数扭子的模 $p$ 参数支撑只有 $s=1,2$。有限 $p$ 幂扭子上的互素主分解给出实际 $R$ 直和

$$
T=T_1\oplus T_2,\qquad S=S_1\oplus S_2.
$$

这里 $T_a$ 表示模 $p$ 参数根 $a$ 的完整主分量，不是仅在点 $s=a$ 取值的核。

既有结果给

$$
T_1\simeq_D D/p\oplus D/p^2,
$$

以及

$$
S_2\simeq_D(D/p^2)^7\oplus D/p^4\oplus(D/p^5)^2\oplus D/p^6,
\qquad\ell_D(S_2)=34.
$$

根一的原九目标在完整 $C/pC$ 中只张成原 $f=[t_2]$ 的 primitive 自由直线，和完整系数扭子像的交为零。这只把尚未确定的 $S_1$ 压到 $pT_1$，没有把它证明为零。本次保留这一可能的隐含 $p$ 进位，并实际计算了它。

## 3. 为什么根一只需八个差列与两层进位

令 $\mathcal O=\mathbf Z_{31}$。所有局部运算在 $C\otimes_D\mathcal O$ 的真实根一完成分量中进行。

[完整原目标湮灭理想](R150-appendix-original-nine-targets-complete-integral-annihilator-and-parameter-denominator-law.md)已付 $x^2B=0$。由于 $x=s-2$ 在根一主分量上可逆，$B_1=0$，即

$$
h_*M_1=0.
$$

原 $h_*$ 在模 $31$ 根一处是简单根。设其 Hensel 根为 $\alpha_1\in1+p\mathcal O$；其余因子在该主分量上为单位，所以

$$
(s-\alpha_1)M_1=0.
$$

因此原九目标已经作为 $\mathcal O$ 模生成全部 $M_1$，无需另加未核的参数幂。已付 primitive 门保证其自由像是 $\mathcal O f$。保留 $f$ 后，只需计算其余八列 $[t_j]$ 相对于同一自由直线的扭子分量。

取完整 $T_1$ 的真实原除源基 $g_1,g_2$，阶分别为 $p,p^2$。本次实际选择的是原十六基的第 $0,2$ 列之根一投影；选择和基的完整性均在全部 315 坐标中重新核验。

对 $W_j=[t_j]$，第一层完整商计算实际给出

$$
W_j\equiv a_{0j}f\pmod{pC_1};
$$

两个扭子坐标均为零。在原来源中求出 $q_{0j}$，然后以完整原整数乘积核验

$$
p^2(t_j-a_{0j}t_2)-A(p^2q_{0j})=p^3r_{1j}.
$$

等式的 Taylor 来源先在十阶上求出；保守使用既有最多五阶的完成精度损失后，$r_{1j}$ 的前五阶是真实有效的。根一完整模 $p$ 商由前三阶就能检测，故第二层的 315 类不丢信息。

第二层完整商写为

$$
[r_{1j}]=d_{1j}g_1+d_{2j}g_2+a_{1j}f+p[r_{2j}].
$$

因而

$$
W_j=(a_{0j}+pa_{1j})f+p d_{1j}g_1+p d_{2j}g_2+p^2[r_{2j}].
$$

这里 $pg_1=0$，$p^2T_1=0$。最后一项可以含自由尾，但它的扭子部分为零；primitive 自由直线保证所有自由尾仍在 $\mathcal O f$。所以原 $W_j$ 的**完整扭子坐标**恰为

$$
(0,\ p d_{2j})\in D/p\oplus D/p^2.
$$

这一步没有把未知自由尾设为零，也没有把 Taylor 完成来源误作已构造的全参数多项式来源。有限 $p$ 幂扭子在忠实完成后不改变，所得有限扭子结论因此返回原 $D$ 模。

## 4. 实际中心一计算及全原检查

本次使用新的中心一源码和新的绑定，直接重放既定全参数原 G/V 来源 DAG，求出真正中心一、十阶的 G/V。没有将根二缓存改名或改头冒作根一。

实际计算包括：

1. 验证原模型、精确整数多项式、F/B 和 G/V DAG、完整状态与两中心商映射的全部输入 SHA；重算原 4433 个方程系数的模 $p^{12}$ 身份。
2. 用原 $(1+t)^d$ 生成纯中心一 Taylor 系数；两中心 CRT 的根一前三槽和根二后五槽字典保持原定义。
3. 对八个原目标及自由修正后的八列，完整核验原 4367 输出、6188 来源和全部整数整除。
4. 用新中心一 G 在全部 1034 行上求解，保留全部自由条件，经原 V、F、B 运输回原 6188 来源，再完整乘回下一层整数余量。
5. 每个相关类通过全部 104 局部自由条件、全部 505 全局自由观测及全部 315 原商重构；根一的整个七维参数主分量均被保留。

共十一阶段全部实际退出零。两层精度为 $10\to5$，第一层两个真实扭子坐标全部为零。第二层在阶 $p^2$ 的真实基轴上产生非零模 $p$ 坐标。因此

$$
\boxed{S_1=pT_1\simeq_D D/p.}
$$

参数 $s$ 在该一维 $\mathbf F_{31}$ 模上作用为 $1$，故还得到准确的 $R$ 模描述

$$
\boxed{S_1\simeq_R R/(p,s-1).}
$$

另一个只读小程序重新哈希全部三十七个阶段输出，核全部 canonical／阶段绑定，使用原主分量数据重新乘回两层的全部 315 坐标。它以整数最大公因数直接确认阶 $p^2$ 轴中八个生成元的公共赋值恰为一，不调用生产程序的 Smith 消元；同时重核 $s$ 在所得 socle 上为恒等。该审计实际完成于 $0.588529271$ 秒，没有重做原求解。

## 5. 全部共同模与生成数

由真实主分解和本次 $S_1$ 结论，

$$
S=S_1\oplus S_2
\simeq_D D/p\oplus(D/p^2)^7\oplus D/p^4
\oplus(D/p^5)^2\oplus D/p^6.
$$

其长度为 $1+14+4+10+6=35$，十二个非零循环因子给 $d_D(S)=12$。根一只需一个局部多项式生成元，根二已经实际付 $d_R(S_2)=8$。有限参数作用代数上的半局部 Nakayama 因此给 $d_R(S)=8$。

正合列

$$
0\longrightarrow S\longrightarrow M\longrightarrow F_M\longrightarrow0
$$

的右项是 $D$ 自由秩二十五，故作为 $D$ 模分裂，得到 §1 的完整结构及 $d_D(M)=25+12=37$。

根一完成分量满足 $(s-\alpha_1)M_1=0$，且有自由秩一加一个 $p$ 扭子，所以其最少局部多项式生成元为二。根二的实际最少生成元仍为八，其余支撑已经由完整自由格资格控制在三以下。因此完整原 $M$ 仍恰需八个多项式生成元。

还可明确区分已完成的两个有限模：$B=h_*M$ 长二十四，而 $S=M\cap T$ 长三十五，所以

$$
\ell_D(S/B)=11.
$$

该长度差不单独确定商的循环因子。不能用九个单目标的循环类型替换共同模，也不能由 $D$ 模分裂删去根二的 $R$ 扩张。

## 6. 实际身份和可复算入口

主入口是 [中心一完整两层源码](../notes/2026-11-16-r150-original-joint-m-root-one-complete-two-digits-789f.py)，精确执行接口见 [两层接口](../notes/2026-11-16-r150-original-joint-m-root-one-two-digit-interface-789f.md)。六个独立 helper 的完整身份随接口保存。全部源码、参数和下列执行身份可入库；数学数组只保存在临时执行目录。

| 对象 | 实际身份 |
|---|---|
| 主源码 | 31388 bytes；SHA256 `9a1188f53fa0a64185e0db3c163231f134d21f0fb5d66718a70f425fe79226d8` |
| 主绑定 | `c7a18e56374d223e1653fd48561d5f5c7dd4d2548e77486bdb4cbd9cf5ffe3df` |
| 完成 raw | 13523 bytes；SHA256 `342f10fce9639bf879e86eb60eea307afa960062ffff28b39315e3892eebbe78` |
| 临时完整坐标文件 | 662 bytes；SHA256 `2598ebf23851c2bd48e2c32049dc5adb9a660984c336698bccd36215ead5fc55` |
| 实际执行 | 2026-11-16 UTC，本地独立目录；退出零；137.637586932 秒 |
| 只读审计源码 | 6745 bytes；SHA256 `14a7a7d38d46c326f4dedcac31096b1f61a6e5b599e0f8ed79e909cad65cd911` |
| 只读审计 raw | 1044 bytes；SHA256 `14b6764cc08a5db1d12f22bf9fb9d22d878203ff8a76d5a9398570ff664ee8c0` |

只读审计源为 [root-one completion audit](../notes/2026-11-16-r150-original-joint-m-root-one-completion-audit-789f.py)，执行身份为 [root-one local completion execution](../notes/2026-11-16-r150-original-joint-m-root-one-local-completion-execution-789f.json)。本次没有重新计算完整 210 来源链，也没有把尚未完成的来源或参数扩张写成结论。
