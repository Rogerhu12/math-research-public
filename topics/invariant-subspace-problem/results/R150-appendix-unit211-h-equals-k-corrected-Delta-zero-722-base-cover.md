# R150：正确 h=k、Delta=0 的新原 Q 投影与至多722个基点

日期：2026-11-28（Asia/Taipei）。会话 Astra-ISP-8542378f-20261127；GPT-6 Astra Pro（AI-assisted）。

**状态：下述准确原图内的有限基点界已证明。** 在原 $h=k,\Delta=0$ 且
$$
ABQ(1-Q)P_f\,bcP_{02}\ne0
\tag{1}
$$
的图中，不同 $(\lambda,u)$ 基点至多 **722** 个。全部 Q 首项为零的专化均包括在内；没有据此给完整 Q 或 Gram 纤维的有限界，也没有排空这个图。$P_f=0$ 补图独立保留。

本结论来自正确 $R_{\mathrm{true}}$ 的新投影。旧错误 Rbad 所导出的848/578覆盖仍撤回，不因本篇得到新界而恢复。

## 1. 真正同一点的必要条件

沿[正确五原行与三个物理 cofactor](R150-appendix-unit211-h-equals-k-corrected-five-original-rows-and-three-physical-cofactor-conditions.md)，令
$$
A=2\lambda^2-2\lambda+1,\qquad
B=4\lambda^3-6\lambda^2+3\lambda-1,
$$
$$
\xi=B/A,\quad\ell=A^3/B^2,\quad T=A^2/B,\quad
h=k=1+\xi,\quad w=\lambda-1-T.
$$
原对称配对为 $p=1+\rho,q=1-\rho,\rho^2=1-Q$，并有
$$
u=bp+cq,\quad m=u-\ell,\quad
bc=\frac14\left(\ell^2-\frac{m^2}{1-Q}\right).
$$
定义
$$
V_2=2u-\ell Q,\quad T_0=V_2-2u^2,\quad
J=2u(1-u)+\ell Q,
$$
$$
\Phi=T_0+4u-4+Q,\quad
P_{02}=(2-3u)V_2-Qu+2u^3,\quad P_f=T_0(J-Q),
$$
$$
G=\lambda P_{02}+(u-1)T_0,\quad
P_c=QP_{02}(\ell+T)-GT_0,
$$
$$
S=2\xi+3-2\lambda,\quad\eta=\xi+3-2\lambda,
$$
$$
N_F=(3-4\lambda)Q+J\xi\eta,\quad
N_C=\eta(-G\xi+Qwu).
$$
在 (1) 中，原 P1 给同一自由 $z=Qt$ 上的
$$
f=-\frac{P_c+bc\Phi z}{P_f},\qquad
NV=N_Ff+bcS\xi z+N_C.
$$
完整原值 $V_{\mathrm{val}}=(1,w,h,h)$ 满足前篇已返回的
$$
Q N_4(V_{\mathrm{val}})=2NV.
$$
置
$$
\Delta=\Phi N_F-S\xi P_f,\qquad
T_n=P_fN_C-P_cN_F.
$$
直接有无 $\Delta$ 逆的原身份
$$
P_fNV=T_n-bc\Delta z.
\tag{2}
$$
所以每个本图原点必须满足 $\Delta=T_n=0$。

正确第一均值组合是
$$
R_{\mathrm{true}}
=4Q(f-u)(v_n-Qf)+bc z^2
+z(4bcuQ-\ell v_n)
+\frac{m}{2(1-Q)}z\{Q(T_0+4uf)-2v_n\},
$$
其中 $v_n=Jf-G+bc z$。这里使用真实 dual 乘法的一阶平方，未采用旧 $-2d_1^2$ 错式。

## 2. 已证 F61 的定义与准确因子支付

前篇已从同一个 $z$ 上的 $(R_{\mathrm{true}},W,O)$ 三原行，按 $(1,z,z^2)$ 系数给完整 cofactor 身份。对原行分母及共同内容只清 (1) 内的支持，再作规定的有理首项归一，所得 $C_1$ 满足
$$
C_1=\frac{(2\lambda-1)^2 Z^3}{56668397794435742564352}\,
F_{61,17,9},
\tag{3}
$$
$$
Z=B^4u^2-2A^3B^2u+A^6Q
=-4B^4bc(1-Q).
$$
$Z$ 在 (1) 非零，$2\lambda-1$ 已由独立的完整物理五列排除支付。因此每个本图原点都满足
$$
F_{61,17,9}(\lambda,u,Q)=0.
\tag{4}
$$
其下标为三变量次数，总次数79，5855项；规范 SHA256 为
69babd37fc45ade649b12b4b849151574080a2bf92c7c2266141d17be1a9d999。

本次只再生这个既有必要输入的确定定义，并核指定 SHA。没有重跑原五行/三 cofactor 证明门，也没有运行旧 N1/NP 投影或已冻的 Loww 两个 z 目标。

## 3. 新的正确第二曲线

清 $\Delta$ 的原分母与当前图已付支持，得
$$
D_2(\lambda,u,Q),\qquad
\deg_{\lambda,u,Q}D_2=(12,4,2).
$$
实际 D2 为98项，其 SHA256 是
6e482757458656b38ee447c7509286fe03dd15fb93d1e45e84fbbeaac0ed66ef。
这个指纹与独立旧 $\Delta,T_n$ 计算的 D2 完全一致。

本次真正的新计算是
$$
M_{\mathrm{raw}}^{\mathrm{true}}
=\operatorname{Res}_Q(D_2,F_{61,17,9}).
\tag{5}
$$
固定 Q 次数为2与9，即11阶 Sylvester 行列式。每个共同有限 Q 根使该固定矩阵奇异；这一必要性在任何首项退化时仍成立，没有除某个 Q 首项。

唯一首次实际精确 QQ 计算得到：

| 对象 | $(\lambda,u)$ 次数 | 总次数 | 项数 |
|---|---:|---:|---:|
| 原新结式 $M_{\mathrm{raw}}^{\mathrm{true}}$ | $(213,40)$ | 253 | 7349 |
| 剥已付 Q 无关支持后的 $M^{\mathrm{true}}$ | $(110,14)$ | 124 | 1664 |

只剥以下已有原证明的支持：
$$
A,\quad B,\quad\lambda,\quad u,\quad u-1,\quad S.
\tag{6}
$$
本次实际 gcd 剥除轮数依次为 $5,28,4,6,20,5$。这是按指定整多项式支持所作的 gcd 轮数，不把它们误写成统一的不可约因子重数。每次整除和最终乘积均核回。

其中 $u\ne0$ 的来源是347c的真实 dual 零基点 mean 全排除及非零共同缩放，详见[静态来源核查](../notes/2026-11-28-unit211-original-u-zero-scaling-static-audit-8542.md)。对称 $u-1$ 仅引用[新整 u=1 原纤维证明](R150-appendix-unit211-h-equals-k-entire-symmetric-u-one-original-exclusion.md)，没有借旧 $p=1$ 规范的 $u_{\mathrm{old}}=1$。$S$ 采用[三份正确原源的静核](../notes/2026-11-28-hk-Szero-true-original-static-source-audit-8542.md)。

不存在一般 $m,\Phi$ 或新几何范数的删除。因此每个本图原点必须有
$$
M^{\mathrm{true}}(\lambda,u)=0.
\tag{7}
$$

## 4. 独立旧相容曲线的准确复用

独立原 $\Delta,T_n$ 已经给
$$
P(\lambda,u)=0,\qquad \deg_{\lambda,u}P=(28,3).
\tag{8}
$$
P 为115项，规范 SHA256：
8af7c105334af350ef5047ee49cf27a5aadbfa204a11b64f9b7f7b8a352dd49c。

这是旧稿中与错误 Rbad 无关的第一条曲线。根已静态比较旧源和正确源中从 $\lambda,u,Q$ 到 $\Delta,T_n$ 的整段定义，字节相同；旧第一投影的实际小回执也明确：

- D2 未剥额外原因子；
- $T_n$ 的原多项式只剥 Q、S 支持；
- 最终 P 只剥 A、B、u、u−1、S 支持。

这些支持现在均由 (1)、(6) 的准确原来源支付。旧第二曲线和它导出的界没有用于本篇。

旧 P 的唯一计算是run46025096446/job140594347573。为不重做这项已登记投影，新工作流按根规矩15只用终端 git 从历史提交 ac40c96b0cfb3758fbf8bd380d18ca288a23601f 取当时回执到 runner 临时目录。新源只在内存中解出指定 SHA 的 P，核其完整规范 SHA 与双次数。没有解出或使用旧错误 M；没有打印、传输、回存或重新提交系数缓存。当前主线已清理的旧回执不变。

在新 $M^{\mathrm{true}}$ 和这个独立 P 上，本次首次精确 QQ 运算实际给
$$
\boxed{\gcd_{\mathbb Q[\lambda,u]}(P,M^{\mathrm{true}})=1.}
\tag{9}
$$
两个相应整除都乘回。式 (9) 排除共同曲线分量；它本身不等于两个曲线没有交点。

## 5. 为什么得到722而非空集

按固定 u 次数3与14构造17阶 Sylvester 矩阵。由 (9)，其行列式
$$
R(\lambda)=\operatorname{Res}_u(P,M^{\mathrm{true}})
$$
非零。本次不需要展开这个更大的结式。矩阵中14行来自 P，$\lambda$ 次数至多28；另3行来自新 M，$\lambda$ 次数至多110。因此
$$
\deg_\lambda R\le14\cdot28+3\cdot110=722.
\tag{10}
$$

还需按不同 $(\lambda,u)$ 点计数。固定 $\lambda_0$，两个专化多项式不可能同时恒为零；否则竖直直线 $\lambda=\lambda_0$ 是共同曲线，与 (9) 矛盾。若该纤维有 r 个不同共同有限 u 根，则至少一个非零专化多项式给 $r\le14$。

在17列固定单项式中，这 r 个根给 r 个线性独立的 Vandermonde 评价列。每一列都在专化 Sylvester 矩阵的核中，故核维数至少 r。用常数可逆行列变换把相应 r 行的常数项置零，即知行列式至少含 $(\lambda-\lambda_0)^r$。于是
$$
\#\{(\lambda,u):P=M^{\mathrm{true}}=0\}
\le\sum_{\lambda_0}\operatorname{ord}_{\lambda_0}R
\le722.
$$
这包括两个 u 首项的全部退化点、竖直特殊纤维以及相交重数造成的额外零。没有用一般点假设删除这些纤维。

每个 (1) 中的原点投到上述集合，故定理成立。这个投影论证不控制每个基点上的 Q、z、完整 Gram 或个别谱纤维；它们仍需原处理。$P_f=0$ 补图也没有由 (10) 排除。

## 6. 唯一实际回执与指纹

[新源](../notes/2026-11-28-unit211-h-equals-k-corrected-Delta-zero-RWO-Q-projection-8542.py)：

- Git blob4e80aedebd40af9b6bc877c0f164d69a2b13f294，9871 B；
- SHA256 3fcc2e90677b7bbd0247d72c1922fc6ed0b60da4ced715a7cecbeae656aade33；
- 只取正确 f33 源5121 B必要定义前缀，SHA256 325c32cb81f37b3f31affd4e98f01c39fcee75b2cc0eae1d9cbb079edaf6d078；
- 唯一run46120122225/job140902587651，内层exit0；
- 驱动1.158840809秒，峰值RSS68600 KiB；
- 新结式在0.896890489秒返回，已付剥除在1.077769574秒完成，实际新 gcd 在1.095181302秒返回；246次精确整除乘回；
- stdout3663 B，SHA256 5a8ec2f31e8ddf356fdde752c631ef9eb6a358f8eb42a8a30dcbf0aa20549fb4；
- 源提交fc9e921ed2e0bc5000f5b67e2beb4e016b8359d5；真实pull至197b8125326cbeeb5ffc30c97bdb7814c31c9a88，2026-11-28 07:12:44.473517 UTC，两份README无变。

原新结式的三变量 Q 次数零格式 SHA256：
95599d7846ce16b022d82286b787ca0709b02ae3916ef49fb43f7c80bc417c7e。

最终 $M^{\mathrm{true}}$ 的同格式 SHA256：
003995ba2eeb0878723965b2404719f1c53ec0ae0f1e4b69da6b4fa38c66f3bc。
移去恒为零的 Q 指数后，双变量格式为98184 B，SHA256：
65d420e901bd60b711d76ad23699daab655414b0595383a19a93d13180f30663。
两者是同一多项式的不同规范编码，不是两条新曲线。

[输入说明](../notes/2026-11-28-unit211-h-equals-k-corrected-Delta-zero-RWO-Q-projection-8542.md)及[小回执](../notes/2026-11-28-unit211-h-equals-k-corrected-Delta-zero-RWO-Q-projection-8542.execution.json)保存准确范围和实际状态。没有保存可重算系数载荷；722界是新正确原投影的基点界，不是普通 Hilbert ISP 的完成结论。
