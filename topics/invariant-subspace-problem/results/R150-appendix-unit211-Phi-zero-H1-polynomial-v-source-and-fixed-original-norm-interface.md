# 一般 Phi=0 的 H1：不倒二次头的全多项式原值输入与固定范数返回

> **2026-11-28 更正：本页经旧紧凑 R2 / Rbar 导出的原必要性、有限性、点数与排除声明已撤回。** 二重点一次坐标的平方被误写为 d1²，真实值为 2d0d1；完整更正和依赖边界见[原定义更正](../notes/2026-11-28-unit211-dual-germ-compact-mean-definition-correction-and-dependency-quarantine-8542.md). 已实跑的旧定义矩阵等式、次数与失败记录保留，不能再据此推原 Gram 条件或支付新模型单位。下文保留为原记录。


日期：2026-11-28（Asia/Taipei）。会话：Astra-ISP-8542378f-20261127。

## 1. 新结论及保留范围

仍在原 $\Phi=0$、物理 $D\ne0$、完整 H1 曲线 $g(u,Q)=0$ 上工作，$g$ 是[原首一 Q 四次式](R150-appendix-unit211-Phi-zero-whole-first-head-Dixon-256-weight-cover.md)。

本篇建立新的全多项式坐标与实际矩阵列，不倒置新的二次头。其主要结论是：

1. 四个完整原二次式在新坐标中经原已付单位清分母，成为 $\mathbb Q[u,Q,\lambda,T,v]/(g)$ 中的多项式。
2. 原三头的伴随矩阵给出真正的缩放乘法列；包括该头行列式为零的全部纤维。
3. 同一点的完整 $F_6$ 和 $N_V$ 给出两个新必要列，并实际产生 $\lambda$ 次数 $6,6,9,10$ 的四条 QQ 原 cofactor。
4. 三个固定正规 Sylvester 行列式的模 1009 返回及严格 QQ 次数上界已经支付；本次没有支付其 QQ 精确次数。

[六非线性极点排空](R150-appendix-unit211-Phi-zero-H1-six-nonlinear-poles-complete-exclusion-and-804-cover.md)所剩的 $P_{201}$ 与至多 804 个不同权对仍是当前严格覆盖。本次模共同因子没有缩小该界。整 H1、整 $\Phi=0$ 和普通 ISP 均未完成。

## 2. 可逆原坐标与四个准确尺度

沿用同一个原点及全部原定义，写旧 $z=Qt$，并令
$$
v=Jf-G+bc\,z,\qquad
f=-P_c/P_f,\quad
G=\lambda P_{02}+(u-1)T_0.
$$
因为 $bc$ 是当前原单位，
$$
z=\frac{v-Jf+G}{bc}
$$
给出原值的双向恢复；没有引入新的值分母。

置
$$
\ell_n=Q-2(u-1)(u-2),\quad
m_n=uQ-\ell_n,\quad a_n=Q-\ell_n,
$$
$$
M_n=\ell_n(2u-\ell_n)-u^2Q=QM.
$$
这里 $\ell_n=Q\ell$、$m_n=Q(u-\ell)$。
进一步定义全多项式
$$
F=GT_0-P_{02}(\ell_n+QT)=P_ff,\qquad
V=vP_f,\qquad W_0=T_0P_f+4uF,
$$
$$
N=QW_0-2V,\qquad Z=V-JF+GP_f=P_fbc\,z.
\tag{2.1}
$$
新源码直接写出四个整数多项式，并与原完整 $R,W,O,N_1$ 逐式乘回：
$$
\boxed{
\begin{aligned}
\widetilde R&=4M_nP_f^2R,\\
\widetilde W&=QP_f^2W,\\
\widetilde O&=(1-Q)Q^2P_f^2O,\\
\widetilde N_1&=QP_f^2N_1.
\end{aligned}}
\tag{2.2}
$$
四个尺度全是原已付单位。该恒等式没有使用二次头、Dixon 坐标首项或范数的逆。

例如，令 $\delta=1-Q$，第一条原多项式准确为
$$
\begin{aligned}
\widetilde R={}&4M_n\big[
(V+a_nuP_f)^2-2uQVP_f+2a_nu^2QP_f^2\\
&\hspace{18mm}-4a_nuQFP_f+4uQZP_f\big]\\
&+16\delta QZ^2-16\delta\ell_nVZ+8m_nZN .
\end{aligned}
\tag{2.3}
$$
其余三条的完整紧凑表达式在[唯一源码](../notes/2026-11-28-unit211-Phi-zero-H1-polynomial-v-source-scaled-matrices-fixed-norm-input-8542.py)中逐项给出，并分别按 (2.2) 核回。

四条均对 $(\lambda,T,v)$ 总次数二。此次实际未约消原多项式各有 10 个几何单项式；在首一 $Q$ 四次余式内，四个最大 $u$ 系数次数分别为 $16,16,19,17$。

随后只删除实际整除各条全部系数的原单位 $u,u-1,Q,1-Q,T_0,J-Q,\ell_n,m_n,M_n$；每次删除都返回完整多项式乘积，且所有余系数仍在 $\mathbb Q[u,Q]/(g)$。没有删除未付的内容因子。以下把这些经已付单位归一的四条仍记为 $R,W,O,N_1$。

## 3. 原头的伴随矩阵与全部零纤维

按 $1,T,v,T^2,Tv,v^2$ 展开四条。取原 $R,W,N_1$ 的后三列为 $H$，令
$$
h=\det H,\qquad C=\operatorname{adj}H.
$$
所有元素均属于完整 $A_0=\mathbb Q[u,Q]/(g)$。实际返回
$$
CH=hI_3.
\tag{3.1}
$$
若前三列为 $\ell_i(\lambda)$，则定义三个列
$$
r_j=-\sum_i C_{ji}\ell_i.
$$
由完整原式得到
$$
hT^2=\mathbf v r_{20},\quad
hTv=\mathbf v r_{11},\quad
hv^2=\mathbf v r_{02},
\qquad \mathbf v=(1,T,v),
\tag{3.2}
$$
每条差都已核回为原 $R,W,N_1$ 的多项式组合。

用 (3.2) 定义缩放矩阵 $M_T,M_v$：它们的后两列由相应 $r_j$ 给出，第一列分别为 $he_T$、$he_v$。在每个原点准确有
$$
\mathbf vM_T=hT\,\mathbf v,\qquad
\mathbf vM_v=hv\,\mathbf v.
\tag{3.3}
$$
这里完全没有除以 $h$。所以 $h=0$ 时仍有同样的真实关系，而 $\mathbf v$ 的第一坐标仍为 $1$。

若 $O$ 的前三列为 $o_{\rm low}$、后三个系数为 $o_{20},o_{11},o_{02}$，定义
$$
r=h\,o_{\rm low}+o_{20}r_{20}+o_{11}r_{11}+o_{02}r_{02}.
$$
实际核回 $hO-\mathbf vr$ 为三个原式的组合。因而原点同一个非零行 $\mathbf v$ 杀掉
$$
r,\quad M_Tr,\quad M_vr,\quad
c_T=(M_TM_v-M_vM_T)e_T,\quad
c_v=(M_TM_v-M_vM_T)e_v.
\tag{3.4}
$$
交换子的第一列准确为零。以上不要求三生成模自由，也不假设两个矩阵在整个代数上交换。

本次 $h$ 的完整四维正规范数确为 101 次 QQ 多项式，原系数定义 5232 字节的 SHA-256 是
cb5c627cf4b7302b0b440a0c6d0c1329c4f6f4fae8ae9c9a0a39f366c4827bf7。
这个范数尚未成为新单位；它的全部零纤维在 (3.1)–(3.4) 中保留。

## 4. 完整同点矩条件与新增必要列

记
$$
A_2=2\lambda^2-2\lambda+1,\quad
B_3=4\lambda^3-6\lambda^2+3\lambda-1,
$$
$$
D=\ell A_2-T^2,\qquad
K=\ell^2B_3-3\ell TA_2+2T^3.
$$
使用此前已付的完整原条件
$$
F_6=MK^2-4(u-\ell)^2D^3=0.
\tag{4.1}
$$
原 $N_V$ 则采用同一点的 $N_F^{(4)}f+N_C^{(4)}+2bcS_nZ_nz$，全部 $N_F^{(4)},N_C^{(4)},S_n,Z_n$ 在源码按已付原公式构造，不单独把两个线性系数置零。

新坐标下实际有
$$
Q^5F_6\in A_0[\lambda,T,v],
$$
$$
Q^2P_fN_V=
Q^2\big[(N_F^{(4)}-2JS_nZ_n)F+
P_fN_C^{(4)}+2P_fS_nZ_n(v+G)\big]
\in A_0[\lambda,T,v].
\tag{4.2}
$$
第二条按完整原 $N_V$ 乘回，不是只保其中一个系数或其范数。

对任一这样的原必要多项式
$$
P(\lambda,T,v)=\sum c_{lab}\lambda^lT^av^b,
\qquad d=\max(a+b),
$$
定义全多项式列
$$
k_P=\sum c_{lab}\lambda^l h^{d-a-b}M_T^aM_v^b e_0.
\tag{4.3}
$$
由 (3.3) 逐次相乘，每个原点满足
$$
\mathbf v k_P=h^dP(\lambda,T,v)=0.
\tag{4.4}
$$
矩阵相乘顺序固定为 (4.3)，不需要任何全局交换。即使 $h=0$，该推理仍成立。
本次实际形成 (4.1)–(4.2) 的两个完整列，再仅用原单位作逐坐标整除归一。

于是形成四条固定三阶 QQ cofactor：
$$
\begin{aligned}
F_0&=\det[r,M_Tr,M_vr],&
F_c&=\det[r,M_Tr,c_T],\\
F_m&=\det[r,M_Tr,k_{Q^5F_6}],&
F_N&=\det[r,M_Tr,k_{Q^2P_fN_V}].
\end{aligned}
\tag{4.5}
$$
源码仍只剥实际整除全部系数的原单位。每个原点同时使这四条为零，所有二次头零支均已包含。
准确返回为：

| cofactor | QQ 的 $\lambda$ 次数 | 最大 $u$ 系数次数 |
|---|---:|---:|
| $F_0$ | 6 | 83 |
| $F_c$ | 6 | 77 |
| $F_m$ | 9 | 129 |
| $F_N$ | 10 | 131 |

## 5. 固定正规 Sylvester 身份与真实次数边界

对 $j=c,m,N$，定义真正的特征零多项式
$$
R_j(u)=
\operatorname{Norm}_{A_0/\mathbb Q[u]}
\operatorname{Res}_{\lambda}^{(6,\deg F_j)}(F_0,F_j).
\tag{5.1}
$$
结果式严格按 (4.5) 的固定次数定义；原点处即使首项退化，也仍给必要条件 $R_j(u)=0$。对每个系数取完整四维正规表示，(5.1) 等于一张 $\mathbb Q[u]$ 多项式矩阵的行列式，阶数分别为 $48,60,64$。

新源对每张矩阵按实际 QQ 系数次数做最大权完美匹配，并返回完整行列对偶
$$
a_i+b_j\ge\deg M_{ij},\qquad
\sum_i a_i+\sum_jb_j=\text{匹配权}.
$$
故得到严格的 QQ 次数上界。所有输入有理系数在 1009 为整，固定行列式可正确约化。模运算虽用 Euclid 求同一个固定结果式，但每次除法、完整四维逆均乘回；最终结果式确回到多项式环。因为 $A_0$ 对 $\mathbb Q[u]$ 自由，泛参数恒等式由此延拓到所有参数，临时 Euclid 主元的零纤维没有被丢弃。

实际结果为：

| 多项式 | 正规阶数 | 已证 QQ 次数上界 | 模 1009 完整次数 | 尚未支付的差 |
|---|---:|---:|---:|---:|
| $R_c$ | 48 | 3596 | 3179 | 417 |
| $R_m$ | 60 | 5764 | 5131 | 633 |
| $R_N$ | 64 | 6092 | 5407 | 685 |

三张对偶最高系数矩阵的模行列式均为零，因此这些上界均不能冒充 QQ 精确次数。本篇没有据此使用保度 Gauss 排除。

三个真实模多项式的共同因子实际次数为 2773，完整模因式乘回已经返回。其中有次数 85、122 的因子，各重数一；其余为次数 $1,2,3,4,5,8$ 的因子，含高重数。这里没有把这些模因子当作 QQ 因子，也没有除掉未在 QQ 支付的原单位范数幂。

## 6. 唯一实际运行及当前接口

- 源：[全多项式原值与固定范数新输入](../notes/2026-11-28-unit211-Phi-zero-H1-polynomial-v-source-scaled-matrices-fixed-norm-input-8542.py)。
- Git blob：0ea9a132ac3d7d98739ddfdc5ef9f8e7393a0a23。
- SHA-256：5f6ba628dd4a660a7cedc7bb338a7cebc9cdc1ac3b6d6958a36409cb578b00ef。
- 首次 run：46069684921；job：140743376887。
- 源提交：05b4971081af6682c62a38bb3334e43741ba6935。
- 限额：120 秒、1 GiB。
- 实际：15.058230470 秒，87836 KiB，退出码 0。
- stdout：26992 字节，SHA-256 8a1030834ba41ae1fdbda65675b8c1784bb88760e50c03fea3b8a0b4012c1f52。

四条新的 QQ 清分母身份在 0.101 秒之前返回；不倒头的六列在 0.496 秒之前返回；随后四个原 cofactor 与三个固定模范数均实际完成，最后数学事件在 14.975722523 秒。源码无历史参数依赖，未执行旧 Dixon Gaussian 或 C256/C55 支持门。

21:20:59.470037 UTC 的真实 pull 从源提交到 a5336137da1e250de09a75d4f6bb9e96defe7389，两份 README blob 均未改变。小回执见[原式与三固定范数执行记录](../notes/2026-11-28-unit211-Phi-zero-H1-polynomial-v-fixed-norm-execution-8542.json)。

下一数学接口包括：原 101 次头范数的真实零纤维、已付原单位的 QQ 分量切分，以及 (5.1) 的完整特征零次数或有限自由返回。本次只登记已经得到的原全多项式接口与实际次数边界；804 权对覆盖保持。
