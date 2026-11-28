# R150 附录：正确 Phi 的整个 ell-half 原分支排除

日期：2026-11-28（Asia/Taipei）。会话：Astra-ISP-8542378f-20261127。AI-assisted，GPT-6 Astra Pro。

**状态：完整原分支排除，唯一首次实际返回。** 在当前正确 $\Phi=0$、distinct-singleton、物理 $D\ne0$ 原图中，整个 $\ell=\tfrac12$ 分支为空。因此此后的当前 Phi 原图可以使用

$$
\boxed{\,2\ell-1\ne0.\,}
\tag{1}
$$

证明合并两项已经实际返回的原身份：前篇的 $C_{20}(u)z\in I_6$，以及本次新的 $C_{32}(u)z^9\in I_6$。两个权多项式的完整 QQ 因式结果直接证明互素，从而给 $z^9\in I_6$；原 $z=Qt$ 已付非零，故整支排除。没有选取某个复权根，也没有遗漏仿射头零、任何 $\lambda$ 值或原值纤维。

整 Phi 仍未闭合，普通 Hilbert 不变子空间问题未完成。式 (1) 的范围仅为上述正确当前原图，不恢复此前撤回的错误 compact 均值后继。

来源见[前篇 C20 直接原证书](R150-appendix-unit211-Phi-zero-corrected-entire-ell-half-direct-original-z-and-20-weight-cover.md)、[本次完整输入](../notes/2026-11-28-unit211-Phi-zero-corrected-ell-half-z-blowup-original-affine-compatibility-8542-input.md)、[唯一源码](../notes/2026-11-28-unit211-Phi-zero-corrected-ell-half-z-blowup-original-affine-compatibility-8542.py)和[小执行回执](../notes/2026-11-28-unit211-Phi-zero-corrected-ell-half-z-blowup-original-affine-compatibility-8542-execution.json)。

## 1. 原系数环与新坐标

在整个 ell-half 上，

$$
\ell=\frac12,\qquad s=u-1,\qquad
Q=4(u-1)(u-2),\qquad \delta=1-Q.
\tag{2}
$$

沿前篇的相同原系数环 $\mathcal A$，只反演已付支持

$$
u(u-1)(u-2)\delta(2u-1)
       \bigl(2(u-1)^2-3\bigr).
\tag{3}
$$

$u$ 来自独立原零基均值排除，$2u-1$ 来自整等权原排除，最后一个因子来自正确整个 B 零支在 (2) 的拉回；这些来源已经在前篇 §1 明列。本文没有先行假设 $2\ell-1$ 是单位。

令

$$
\epsilon=\lambda-\frac12,\qquad
\tau=T+\frac12,\qquad z=Qt.
\tag{4}
$$

原完整 Gram 的同点恢复仍是

$$
\begin{aligned}
m&=u-\tfrac12,&M&=-2s^2,&bc&=-\frac{s^2}{2\delta},\\
T_0&=-4s^2,&J&=-4s,&P_{02}&=4s^2(u-2),&
P_f&=16s^4,\\
f&=\frac u2-(u-2)\epsilon-\frac{(u-2)^2}{s}\tau.
\end{aligned}
$$

特别 $V-f=(u-2)\tau+bct$、$A_1=-2(u-2)\tau$ 是整式身份，并未置 $\tau$、$A_1$ 或 $t$ 为零。

由[正确整个 t 零原排除](R150-appendix-unit211-Phi-zero-true-entire-tzero-original-exclusion.md)，当前物理图中的 $z$ 非零。于是本次可以作真实双向坐标

$$
r=\tau/z,\qquad \tau=rz.
\tag{5}
$$

唯一新增坐标除法来自这个已经支付的 $z$，没有反演新的头系数。

## 2. 三条真均值成为原仿射式

六个未约化的完整原方程固定为

$$
(F_1,\ldots,F_6)
=(E_1,E_{B,e},E_{B,o},N_1,NS,PS).
\tag{6}
$$

它们使用真 dual 乘法 $(vw)_1=v_0w_1+v_1w_0$；$E_1$ 的平方项是 $-4d_0d_1$。N1 是同一个完整 $N_4$ 的极化，NS、PS 是两个 singleton 的完整 weighted N/P 原值。源只从前篇源码读取 6013 字节必要原定义，截断位置在旧二十坐标矩阵之前。

记 $D_i(u)F_i$ 为六个原分子，$D_i$ 仅含 (3) 的已付支持。本次没有仅根据低次数猜测可除 $z$，而是另核前三式原 $\epsilon$ 次数至多一，再对每一式实际精确返回

$$
D_iF_i(u,\epsilon,rz,z)=zL_i(u,r,\epsilon,z),
\qquad 1\le i\le3,
\tag{7}
$$

$$
L_i=a_i(u,r)\epsilon+b_i(u,r)z+c_i(u,r).
\tag{8}
$$

三式都逐项重组并整式乘回。N1 的 $\epsilon^2$ 项则明确非零并完整保留；没有把第四原式也强行当作仿射式。

令

$$
J=(L_1,L_2,L_3,P_4,P_5,P_6),
\qquad
P_i=D_iF_i(u,\epsilon,rz,z)\ (i\ge4).
\tag{9}
$$

$P_4$ 为完整二次，$P_5,P_6$ 为完整三次。式 (7)–(9) 只在原已付 $z$ 图中使用；最终还会把所有 $z$ 逆清回正幂原身份。

## 3. 所有仿射头零纤维保留的十个兼容式

取三行 $(c_i,a_i,b_i)$ 的矩阵 $H$，其第一列余子式给完整原身份

$$
R_0=\det H=\sum_{i=1}^3\gamma_iL_i.
\tag{10}
$$

没有反演 $\det H$。

对三个固定对 $(i,j)=(1,2),(1,3),(2,3)$，令

$$
\Delta_{ij}=a_ib_j-a_jb_i,\quad
E_{ij}=b_ic_j-b_jc_i,\quad
Z_{ij}=a_jc_i-a_ic_j.
$$

实际原式为

$$
\Delta_{ij}\epsilon-E_{ij}=b_jL_i-b_iL_j,
\qquad
\Delta_{ij}z-Z_{ij}=-a_jL_i+a_iL_j.
\tag{11}
$$

每个 $\Delta_{ij}$ 的整零面继续保留。

对 $P=P_4,P_5,P_6$，分别以固定次数 $d=2,3,3$ 写

$$
P=\sum_{a+b\le d}p_{ab}(u,r)\epsilon^az^b.
$$

对应必要式为

$$
R_{P,ij}
=\sum_{a+b\le d}p_{ab}E_{ij}^aZ_{ij}^b
              \Delta_{ij}^{d-a-b}.
\tag{12}
$$

源用有限几何和构造完整多项式 $U,V$，返回

$$
R_{P,ij}
=\Delta_{ij}^dP-U(\Delta_{ij}\epsilon-E_{ij})
                 -V(\Delta_{ij}z-Z_{ij}).
\tag{13}
$$

代入 (11)，每一条均具有六个 $J$ 生成元的完整原乘子。只有这些实际乘子全体都有公共多项式因子时，才同步精除右侧及所有乘子，再完整乘回；不把那个公共因子支付为单位。

本次一个三阶兼容式加九个 (12) 全部返回，共二十次原来源乘回。N1、NS、PS 的九条身份都覆盖仿射系数矩阵秩零与秩一的纤维。

## 4. 实际只用前三均值与 N1 的新 Bézout

实际 $R_0$ 的次数为 $(\deg_u,\deg_r)=(27,4)$，有 110 项；规范 SHA256 为

$$
\texttt{9a2a3bfb198974008ec1347c9c34a0e6c5420860333578109c46830525198488}.
$$

第一条 N1 兼容式 $R_{N1,12}$ 的次数为 $(42,6)$，有 238 项；规范 SHA256 为

$$
\texttt{d993d162460e543bbe564bb937a36c18a0731b7f1ec720183f7caa4194e0fc34}.
$$

固定顺序的 $\mathbb Q(u)[r]$ 完整 Euclid 在这两条就结束：从 $r$ 次数四降到次数零。源码记录 usedScalarIndices 为 $[0,1]$，因此本次最终新权覆盖实际只使用前三均值与 N1；其余八条新兼容式已经返回，但没有被假称为最终组合的必需输入。

每次短除与 Bézout 来源都乘回。仅清实际最终 Bézout 乘子的纯 $u$ 分母，得到

$$
C_0(u)=A(u,r)R_0+B(u,r)R_{N1,12}
      =\sum_{i=1}^6 A_i(u,r,\epsilon,z)J_i.
\tag{14}
$$

未付纯 $u$ 主元没有因此成为物理单位。对十条兼容式的全向量组合返回，保证未选输入的乘子确为零。

## 5. 回到完整原变量，实际正幂为九

将 $r=\tau/z$ 代回 (14)。前三个 $J_i$ 还具有 (7) 的额外 $z^{-1}$。源码逐单项式计算清除这些分母所需的正幂，实际为

$$
N=9.
$$

乘回原 $D_i$，合并六个完整原乘子，然后只取消它们与右侧 $C_0$ 的真实公共纯 $u$ 因子。此次取消因子次数七，规范 SHA256 为

$$
\texttt{bee0a49f985fba557ba4b6f6ddc05e846579fb56eb32fe544bd99ba4a2a8912c}.
$$

最终在原已付系数环中，两次完整原多项式返回给出

$$
\boxed{\ C_{32}(u)z^9\in I_6.\ }
\tag{15}
$$

这里先返回清原 $D_i$ 共同分母后的全部多项式，再只剥 (3) 的原单位。没有只返回某个余式、模点或泛型矩阵秩。

$C_{32}$ 次数为三十二、项数三十三，规范 SHA256 为

$$
\texttt{0ee79b10006189416882aeaacb606f0bd2e9be84ecf313380bdcac6a7271f424}.
$$

所有未知纯 $u$ 极点都已经进入该多项式，而不是被忽略。

## 6. 完整 QQ 因式直接关闭旧 C20 的全部根

前篇已实际证明

$$
C_{20}(u)z\in I_6,
\tag{16}
$$

且首一 $C_{20}$ 在 $\mathbb Q[u]$ 不可约，次数二十、重数一，其规范 SHA256 为

$$
\texttt{01e360b988892d68755864adae1520933535e6c79faf79bb667f1eec33eeb3cb}.
$$

本次在完成 (15) 后继续作新 $C_{32}$ 的首次完整 QQ 因式分解，并全乘回，得到

$$
C_{32}=H_{20}H_6^2
\tag{17}
$$

的首一归一；两个因子均是实际 QQ 因子。$H_{20}$ 有二十一项，规范 SHA256 为

$$
\texttt{ed7347d97acf89b193df68495bc0f8232a90e6a2f36fd931cdd8d416e9bb295e},
$$

$H_6$ 有七项，规范 SHA256 为

$$
\texttt{d6ca505db7a8dfb48b5b22bbdfdfe73f51792f78e4bf371af7f484e69ee14765}.
$$

前后参数使用同样的四元指数数组、相同有理系数字符串与首一归一；纯 $u$ 多项式的后三个指数均为零。因此不同的二十次规范 SHA 确定 $H_{20}\ne C_{20}$，不是把不同归一的参数作比较。又因 $C_{20}$ 的真实 QQ 不可约性及 $\deg H_6=6$，

$$
\gcd_{\mathbb Q[u]}(C_{20},C_{32})=1.
\tag{18}
$$

这是两次已经完成的完整 QQ 因式结果的直接代数推论，不需要重跑旧覆盖或另开一个 gcd 门。

在 PID $\mathbb Q[u]$ 中存在多项式 $a,b$ 使 $aC_{20}+bC_{32}=1$。由 (15)、(16)，

$$
z^9=a(u)z^8\bigl(C_{20}z\bigr)
       +b(u)\bigl(C_{32}z^9\bigr)\in I_6.
\tag{19}
$$

最后应用当前物理图的已付 $z\ne0$，得到矛盾。因此 (2) 的整个原物理支为空。

这一步同时处理旧 C20 的所有二十个复嵌入、全部 $\lambda,T,z$ 原值，以及恢复 $\rho^2=\delta$ 的两个分支；没有逐根选择或将一个模因子当作特征零分支。$\ell=\tfrac12$ 的碰撞边界代数没有被当成物理解移入当前 $D\ne0$ 图。

## 7. 唯一实际执行与后续新单位

唯一实际 [run 46143529198 / job 140974503932](https://github.com/Rogerhu12/math-research-public/actions/runs/46143529198/job/140974503932) 完整返回：

- 数学阶段 0.709371267 秒；driver 0.776536771 秒。
- driver 峰值 48172 KiB，源退出码 0；原 120 秒、1 GiB 预算不变。
- 三个原仿射式、十八次头零线性身份乘回、二十次新兼容式来源返回、九个 Euclid/Bézout 返回及两次最终完整原式返回均已完成；精确多项式除法乘回计数为 122。
- 源 blob f77b3eb1163c1606c4eddc4e7f4e8a8c3d920b2d；源 SHA256 为 965aa4db96787a17f8f1772929d80adf7e6e9a7ef91eb4643b89e9a63e150b32。
- 源提交 3d476b57175e6ef3123f9bb17c9a31a83269bc14，实际 pull 后为 6e60b15a479d3ca8af57153ffbd59d3c3283b79a，两份规则未变。
- 原 stdout 9935 字节，SHA256 为 c7a8ef2f486fbb50346a442818ca1734aae1c538714a1f888ca31a028676437a。

没有重放前篇二十坐标原 z 目标、C114 的 gcd 或三十列；没有保存可再生系数载荷或编码分片。

当前正确 Phi 余图由此新支付 $2\ell-1$。后续可以在原来已经支付的系数环中再使用这一非零量，继续新的完整个别值或原几何输入；整 Phi、其它碰撞图和普通 ISP 的未闭部分仍保留。
