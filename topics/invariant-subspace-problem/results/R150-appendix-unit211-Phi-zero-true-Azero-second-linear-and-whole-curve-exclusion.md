# R150 补充：正确 Phi 的第二条 A=0 原线性支与整曲线排除

日期：2026-11-28（Asia/Taipei）。会话：Astra-ISP-8542378f-20261127。AI-assisted，GPT-6 Astra Pro。

## 1. 完整结论

在当前正确原 unit211 的
$$
\Phi=0,\qquad Q(1-Q)P_fP_{02}bcD\ne0,\qquad\lambda\ne0
$$
图中，整 $t=0$ 已由真原式排除。令
$$
A=4(u-1)^2-Q.
$$
本条证明
$$
\boxed{A\ne0.}
\tag{1}
$$
本条不使用被撤回的旧 $R_{\rm bad}$、first-head、H1/H42 或其权单位。它先排空[正确 A=0 第一线性支](R150-appendix-unit211-Phi-zero-true-Azero-first-linear-branch-exclusion.md)留下的第二线性支，再合成 (1)。

## 2. 原 A=0 的第二支与完整恢复

沿用
$$
s=u-1,\quad r=u-2,\quad b_0=2u-1,\quad h=2u-3,\quad
\xi=\frac{ut}{2b_0},\quad k=2\lambda-1.
$$
原关系精确给
$$
Q=4s^2,\quad \ell=\frac{u}{2s},\quad
1-Q=-hb_0,\quad bc=\frac{u^2}{4sb_0},
$$
$$
P_{02}=4us^2,\quad P_f=16us^3.
\tag{2}
$$
所以 $u,s,b_0,h,\xi$ 都由原图支付。正确均值的两线性因子已经完整返回；第一支已排，第二支是
$$
f=u-u\lambda-\xi/2,\qquad
T=\frac{\xi-u}{2s},\qquad
t=\frac{2b_0\xi}{u},\qquad A_1=-\xi.
\tag{3}
$$
不倒 $\lambda$ 的另一个一次式或新的权头。

同一真实 Gram 由
$$
\rho^2=-hb_0,\quad p=1+\rho,\quad q=1-\rho,
$$
$$
b=\frac{u}{4s}\left(1-\frac{\rho}{b_0}\right),\quad
c=\frac{u}{4s}\left(1+\frac{\rho}{b_0}\right)
$$
及
$$
x=u-b_0\lambda,\quad y=\frac{r+\lambda+\xi}{h},
\quad X=x+y\rho,\quad Y=x-y\rho
\tag{4}
$$
恢复。令 $a_w=1-\ell$、$r_G=X-a_wp-ct$、$s_G=Y-a_wq-bt$，使用四行
$$
(0,0,p,q),\quad(0,A_1,r_G,s_G),\quad
(p,r_G,0,t),\quad(q,s_G,t,0).
\tag{5}
$$
源码完整返回 $E_0/N_0/P_1$、真实 $E_1-E_W$ 以及共轭关系。形式二次代数同时保留两个 $\rho$，没有取单个数值嵌入。

## 3. 原均值与 N1 的精确首一代数

在 (5) 中，两个 singleton 均值只需一条；另一条是其已付权倍。移去明确的原单位后，记其原多项式为 $E$，原极化 N1 为 $N$。定义
$$
C=\xi^2+us k^2-u,
$$
$$
L=(4s\lambda-1)\xi-2s^2k^2+u.
\tag{6}
$$
本次完整返回
$$
N=C+L,\qquad
E-(4u-3)N=-hL.
\tag{7}
$$
因 $h$ 已付，(7) 是原理想的双向身份，给
$$
(E,N)=(C,L).
\tag{8}
$$
这里的负号保留；一个早期未发布诊断曾误写正号，已准确记录为工程失败，不曾据此返回排除结论。

在环
$$
R=\mathbb Q[u,(us b_0h)^{-1},\lambda]
$$
上，$C$ 对 $\xi$ 首一二次。因此先只模 $C$ 的代数由 $1,\xi$ 自由生成，完整原后续商不被假定自由。记
$$
c_0=us k^2-u,\quad d=4s\lambda-1,\quad
l_0=u-2s^2k^2,
$$
所以 $C=\xi^2+c_0$、$L=l_0+d\xi$。

另一个可直接核对的同点身份是
$$
D\equiv \frac{\xi(u-\xi)}{2s^2}\pmod{(C,L)}.
\tag{9}
$$
终证没有倒 (9)，也没有以模判别式零推出原判别式零。

## 4. 完整 weighted N/P 的两个一次余式

使用同一个 (5)，构造完整原条件
$$
S_{\rm raw}=bN_4(g_B)+cN_4(g_C)
-2\lambda P_{02}(\ell+2T+A_2),
$$
$$
P_{\rm raw}=bP_2(g_B)+cP_2(g_C)
-P_{02}(\ell+3T+3A_2+B_3).
\tag{10}
$$
只清除 (2) 的分母、移去非零有理常数及已付单位，得到原多项式 $S,P$。本次以首一 $C$ 作完整短除法，返回
$$
S=q_SC+S_0+S_1\xi,\qquad
P=q_PC+P_0+P_1\xi.
\tag{11}
$$
全部四个余系数由原 (5)、(10)、(11) 定义，不来自预存系数表。

三个真实一次关系的系数向量是
$$
r_0=(l_0,d),\quad r_1=(S_0,S_1),\quad r_2=(P_0,P_1).
\tag{12}
$$
各自的真实 $\xi$ 倍为 $(-c_0r_{i1},r_{i0})$。这给首一二次代数内完整六行关系，没有用裸矩阵冒充原理想。

任一原点的 $(1,\xi)$ 同时湮灭 (12)，故三个固定二乘二行列式
$$
M_{01},\quad M_{02},\quad M_{12}
\tag{13}
$$
都为零。每个 (13) 都是两条原一次式的完整组合；没有需要先付的矩阵主元。

同时由 $L=0$ 与 $C=0$，
$$
l_0^2+c_0d^2=0.
\tag{14}
$$
(14) 是固定二次范数的完整多项式身份，不把它的非零值作单位。在它及 (13) 中只删除原 $u,s,b_0,h,\lambda$ 的实际整因子，得到四个必要多项式
$$
F,\quad G_{01},\quad G_{02},\quad G_{12}.
$$
实际次数分别为
$$
\deg_{u,\lambda}F=(3,4),\quad
\deg_{u,\lambda}G_{01}=(4,4),\quad
\deg_{u,\lambda}G_{02}=(5,4),\quad
\deg_{u,\lambda}G_{12}=(5,5).
\tag{15}
$$
为便于直接重建，未作有理常数归一前，(14) 除去已付因子 $s$ 恰为
$$
-u(4u-9)-4uhk+u(h^2-8s)k^2+4ushk^3+4s^2b_0k^4.
\tag{16}
$$

## 5. 保所有首项零的三个 QQ 投影

对同一个 $F$，分别与三个 $G_{ij}$ 作关于 $\lambda$ 的固定次数 Sylvester 行列式：
$$
R_{01}=\operatorname{Res}^{(4,4)}_\lambda(F,G_{01}),\quad
R_{02}=\operatorname{Res}^{(4,4)}_\lambda(F,G_{02}),\quad
R_{12}=\operatorname{Res}^{(4,5)}_\lambda(F,G_{12}).
\tag{17}
$$
矩阵阶数是 $8,8,9$，实际所得 QQ[$u$] 次数是 $26,30,33$。

任何原点有同一个有限 $\lambda$ 根，故 (17) 都为零。这里始终使用这些固定矩阵；在某个 $u$ 上的原 $\lambda$ 首项降次只会使矩阵更奇异，不会丢掉该点。没有以泛型 Euclid 反演这些 $\lambda$ 首项。

本次完整 QQ 结果是
$$
\boxed{
\gcd_{\mathbb Q[u]}(R_{01},R_{02},R_{12})
=\frac{(u-1)^3(2u-3)^4}{16}.
}
\tag{18}
$$
每轮完整 Bézout 都已乘回；累计 gcd 次数准确为 $26\to13\to7$。右侧两个因子都是 (2) 已付原单位。于是三个必要投影不能在任何当前原点同时为零，第二线性支 (3) 全部排空。

这使用的是完整特征零 QQ 返回，没有从单素数空性、普通 gcd 为 1 的二维观察或有限候选数推出排空。

## 6. 整 A=0 合成与新范围

前篇 (4) 的两个线性因子完整覆盖整 $A=0$。第一支已独立排除，第二支由 (18) 排除，故 (1) 成立。

因此正确三均值头
$$
\det H=\frac{ABM_n^3L^4}{8K^3(1-Q)^4}
$$
在当前 Phi 图只余 $B=0$ 这条首项零曲线。正确六乘二呈示中的新斜率曲线 $G=0$ 仍须保留。本条不将 $B$ 或 $G$ 当作已付单位，不恢复被撤回的旧 Phi 后继。

## 7. 首次实际小证书

[自含源](../notes/2026-11-28-unit211-Phi-zero-true-Azero-second-linear-fixed-lambda-original-return-8542.js)：

- 源码 SHA256 4b90b10d5e6e0654080b4387aeaf90ae465c46d4911bb6b086c05f1f3ea933a2；
- 16136 字节，纯 V8 BigInt 有理多项式运算；
- 首次实际 61279 ms；
- 5564 次整数多项式乘法、70 次原线性因子完整除法返回；
- 484 次固定 Sylvester Bareiss 精确除法，每一项完整乘回；
- 1456269 次有理运算、7377 次一元多项式乘法、519 次完整除法返回；
- 三投影及 (18) 全部完成，剩余原权多项式为 $1$。

[小回执](../notes/2026-11-28-unit211-Phi-zero-true-Azero-second-linear-fixed-lambda-original-return-execution-8542.json)保存源身份与实际返回。该源只证明第二支；整 $A=0$ 结论由两份已经完成的原证明合成，没有修改执行标志冒充整 Phi 已闭。独立静态复核确认 (7) 的符号、首一二次的完整两个原值余式、固定 8/8/9 阶 Sylvester、仅已付单位的末 gcd；冻结成功代码和执行身份保持原样。整个 Phi、普通 ISP 仍未完成。
