# R271 附录：三加三权组的原联合来源预算与七位统一首末边

- 日期：2026-11-28（Asia/Taipei）
- 会话：Astra-ISP-8542378f-20261127
- 范围：六位原正权 $(\sqrt t,\sqrt t,\sqrt t,1,1,1)$，$t>0$；同一整个出生二上来源和出生一下来源。
- 新增：原联合来源的统一 $1/3$、$1/2$ 费用，以及加任意一位后整个十四维来源的统一定量首末边。

[两组加一位的旧全出生全高度定理](R239-appendix-two-weight-groups-one-exceptional-all-births-all-heights-strict-bound.md)
已包含本篇七位族的严格系数一相邻性。
[R288](R288-appendix-birth-two-s1-short-sides-hard-top-and-full-physical-layer.md)
与 [R292](R292-appendix-main-parameter-s2-and-all-two-exceptional-birth-two-first-edges.md)
还已支付更广权族的定性 S1/S2。
本篇不重新登记这些定性结论；下列统一费用和原相邻比的统一数值余量才是新增部分。

## 1. 原对象与结论

使用 [R275 原三块接口](R275-appendix-first-edge-three-block-equivalence-and-parameter-free-sos.md) 的实际 Hilbert 范数，令
$$
K=\ker d\cap H_2,\qquad L=\ker d\cap H_1,
$$
$$
G_j=P_KF_{j,2}^{-1}|_K,\qquad
L_j=P_LF_{j,1}^{-1}|_L,\qquad
F_{j,k}=\frac{d^jd^{*j}}{(j!)^2}\bigg|_{H_k}.
$$
所有逆先在整个物理层上取。置
$$
C_1=G_1^{-1},\quad C_2=G_2^{-1},\quad F=C_1^2-C_2,\quad
B=d_{b^3}|_K:K\longrightarrow L,
$$
$$
\Delta=\frac12(C_1B^*L_3-B^*L_2),\qquad
A=\frac12(C_1B^*L_2+B^*L_2L_3^{-1}L_2),
$$
$$
\mathsf S=A^*G_1A+L_1L_2^{-1}L_1.
$$

**定理 1。** 在全部 $t>0$，整个九维 $K$ 和五维 $L$ 上有
$$
\boxed{
F>\frac23C_1^2,\qquad
0\le\Delta L_3^{-1}\Delta^*<\frac13F,\qquad
0<\mathsf S<\frac12I_L .
}
\tag{1.1}
$$
$1/3$ 的来源费用常数是尖锐上确界，见 §5。
最后一项只称为已付一致上界，不声称最佳。
共同正倍数缩放全部物理权时，前两个不等式两侧同乘第四次方，$\mathsf S$ 不变。

**定理 2。** 对任意 $a,t>0$ 的七位权
$$
(a,\sqrt t,\sqrt t,\sqrt t,1,1,1),
$$
整个十四维 $K_2$ 的两个合法内部高度均满足
$$
\boxed{
\Gamma_j\Gamma_{j+1}^{-1}\Gamma_j
\preceq c_*\Gamma_{j-1},\quad j=1,2,\qquad
c_*=1-\frac13\left(1-\frac1{\sqrt3}\right)
                  \left(1-\frac1{\sqrt2}\right)<\frac{24}{25}.
}
\tag{1.2}
$$
因此 (1.2) 是该整族原相邻比的统一定量加强，而不是把辅助 Schur 正性直接当作原度量下的余量。

## 2. 两组三位的完整正交分解

每组三位的等权下降按真实正交 primitive 串分解。
组内出生仅为 $0,1$；其串长度分别为 $3,1$，重数分别为 $1,2$。
第一组权为 $\sqrt t$，第二组权为 $1$。

固定两条串，其长度记为 $p,q$。以
$$
w_{i,\ell-i}
=\frac{d_A^{*i}}{i!}\frac{d_B^{*(\ell-i)}}{(\ell-i)!}u
$$
作为相对总孔层 $\ell$ 的去权坐标，$u$ 为单位原组内 primitive。
这些坐标相互正交，实际平方范数为
$$
t^i\binom pi\binom q{\ell-i}.
\tag{2.1}
$$
其下降系数为
$$
d_Aw_{i,k}=t(p-i+1)w_{i-1,k},\qquad
d_Bw_{i,k}=(q-k+1)w_{i,k-1}.
$$
两组权恒定，所以此分解同时约化 $d,d^*$、三次下降、
全部完整 Gram、完整逆以及 primitive 压缩。

上、下来源的全部非空块如下：

| 组内出生 | 串长 $(p,q)$ | 上相对出生 | 上重数 | 下相对出生 | 下重数 |
|---|---|---:|---:|---:|---:|
| $(0,0)$ | $(3,3)$ | $2$ | $1$ | $1$ | $1$ |
| $(1,0)$ | $(1,3)$ | $1$ | $2$ | $0$ | $2$ |
| $(0,1)$ | $(3,1)$ | $1$ | $2$ | $0$ | $2$ |
| $(1,1)$ | $(1,1)$ | $0$ | $4$ | 无 | $0$ |

这里每个所列相对 primitive 空间为一维。
上、下维数分别合为 $1+2+2+4=9$ 和 $1+2+2=5$，
即原完整 $\binom62-\binom61$ 和 $\binom61-\binom60$。
没有删去一般物理层的非固定来源。

$(1,3)$ 块正是[一特殊权实际来源公式](R271-appendix-one-special-weight-all-births-uniform-joint-source-budgets.md)
中的 $r=3$ 活跃块；$(3,1)$ 经交换两组及共同缩放，使用同一公式的 $t^{-1}$。
这些块有
$$
F>\frac23C_1^2,\qquad
\Delta L_3^{-1}\Delta^*<\frac19F,\qquad
\mathsf S<\frac12I.
\tag{2.2}
$$
前两界也见[六位一特殊权完整 S1](R271-appendix-six-site-one-special-weight-full-s1-and-relative-source-margin.md)。
$(1,1)$ 真空块的桥为零，且
$$
C_1=t+1,\quad C_2=t,\quad
F=t^2+t+1\ge\frac34C_1^2>\frac23C_1^2.
\tag{2.3}
$$
因此只需完整支付 $(3,3)$ 的同一上下固定源。

## 3. 固定源的全部完整 Gram 与真正伴随

在相对层 $\ell$，按第一组孔数 $i$ 递增排列坐标。
原除阶下降 $D_j=d^j/j!$ 与按 (2.1) 取的实际伴随为
$$
(D_j)_{r,i}
=t^{i-r}\binom{3-r}{i-r}
           \binom{3-\ell+r}{j-i+r},
\qquad
(D_j^*)_{i,r}
=\binom ir\binom{\ell+j-i}{\ell-r}.
\tag{3.1}
$$
不合法组合数为零，只取实际存在的输入、输出层。
特别地，下三阶的完整输入层为相对四孔层，维数三；
它的全部三列都保留，没有先压到某条试探前像。

下、上 primitive 方向分别是
$$
g_L=(t,-1),\qquad g_K=(3t^2,-2t,3).
\tag{3.2}
$$
其实际范数为
$$
\|g_L\|^2=3t(t+1),\qquad
\|g_K\|^2=9t^2(3t^2+4t+3).
\tag{3.3}
$$
由 $d_{b^3}=td_A+d_B$，逐列得到
$$
Bg_K=6t(1-t)g_L,\qquad
BB^*=\frac{12t(t+1)(t-1)^2}{3t^2+4t+3}
\tag{3.4}
$$
作为低一维空间上的实际标量。

下三个完整 Gram 是
$$
F_{1,1}=
\begin{pmatrix}4+3t&3t\\3&3+4t\end{pmatrix},
$$
$$
F_{2,1}=
\begin{pmatrix}
3+12t+3t^2&6t+6t^2\\
6+6t&3+12t+3t^2
\end{pmatrix},
$$
$$
F_{3,1}=
\begin{pmatrix}
9t+12t^2+t^3&3t+12t^2+3t^3\\
3+12t+3t^2&1+12t+9t^2
\end{pmatrix}.
\tag{3.5}
$$
上两个完整 Gram 是
$$
F_{1,2}=
\begin{pmatrix}
3+3t&6t&0\\
2&4+4t&2t\\
0&6&3+3t
\end{pmatrix},
$$
$$
F_{2,2}=
\begin{pmatrix}
9t+3t^2&9t+12t^2&3t^2\\
3+4t&3+16t+3t^2&4t+3t^2\\
3&12+9t&3+9t
\end{pmatrix}.
\tag{3.6}
$$
这些矩阵在实际非标准度量下自伴；不能以普通转置替换 (3.1)。

简记正多项式
$$
u=t^2+3t+1,\quad v=t^2+8t+1,\quad c=3t^2+4t+3,
$$
$$
d=t^4+4t^3+10t^2+4t+1,\quad
e=t^2+1,\quad q=(t+1)c.
$$
先对 (3.5)–(3.6) 全部求逆，再用 (3.2) 和 (3.3) 压缩，准确得到
$$
\boxed{
L_1=\frac uq,\quad L_2=\frac v{3d},\quad
L_3=\frac u{tq},\qquad
G_1=\frac d{qe},\quad G_2=\frac1t .
}
\tag{3.7}
$$

## 4. 同一来源下的两个完整费用

置
$$
h=3ue-tv,\qquad k=3ue+tv,\qquad
f=q^2e^2-td^2.
$$
由 (3.7) 得
$$
C_1=\frac{qe}{d},\qquad C_2=t,\qquad F=\frac f{d^2}.
\tag{4.1}
$$
把 (3.4) 与全部实际 $L_j,G_j$ 同时代入原式，保留两种来源和两个交叉项，得到
$$
\boxed{
\Delta L_3^{-1}\Delta^*
=\frac{(t^2-1)^2h^2}{3ud^2},
\qquad
A^*G_1A
=\frac{t(t^2-1)^2v^2k^2}{27eu^2d^3}.
}
\tag{4.2}
$$
同一个低源中的剩余项为
$$
L_1L_2^{-1}L_1=\frac{3u^2d}{vq^2}.
\tag{4.3}
$$
没有把 $A^*G_1A$ 换成迹、单列预算或不同 primitive 投影的和。

## 5. 三条全域正多项式证书

首先，直接恒等式
$$
q^2e^2-4td^2=(t-1)^2p_8(t)
$$
中，$p_8$ 的升幂系数为
$$
(9,56,180,360,470,360,180,56,9).
\tag{5.1}
$$
所以固定块有 $F\ge3C_1^2/4$，在 $t=1$ 允许等号。

其次，
$$
uf-(t^2-1)^2h^2=t\,p_{10}(t),
$$
其中 $p_{10}$ 的升幂系数是
$$
(20,199,588,732,896,1130,896,732,588,199,20).
\tag{5.2}
$$
全部严格正，故同一固定块
$$
\frac{\Delta L_3^{-1}\Delta^*}{F}
=\frac{(t^2-1)^2h^2}{3uf}<\frac13.
$$
当 $t\downarrow0$ 时该比趋于 $1/3$，
所以整个三加三族的这一来源常数不能统一减小。

最后，在正分母
$$
D_{26}=54eu^2d^3vq^2
$$
上，$\frac12-\mathsf S$ 的完整分子为
$$
P_{26}
=27eu^2d^3vq^2
-2t(t^2-1)^2v^3k^2q^2
-162eu^4d^4.
\tag{5.3}
$$
它是回文多项式，升幂系数 $[t^j]P_{26}$ 对 $0\le j\le13$ 依次为
$$
\begin{aligned}
(&81,2754,38124,313146,1800417,8017768,29194677,\\
 &88528306,223981726,473233870,839324581,1259071764,\\
 &1605639658,1741706256),
\end{aligned}
\tag{5.4}
$$
其余由 $[t^{26-j}]P_{26}=[t^j]P_{26}$ 给出。
全部二十七个系数严格正，故整个 $t>0$ 域有 $\mathsf S<1/2$。
这是完整交叉来源的有理恒等式，不是正参数样本检查。

由 §2 的全部正交块，(5.1)–(5.4) 立即合成定理 1。

## 6. 返回七位原度量的统一余量

对任意加入位权 $a>0$，旧六位正是定理 1 的整个原空间。
[六独立权出生一内部 half](R271-appendix-six-site-internal-half-complete-ordered-difference-certificate.md)
支付同一旧低源的实际第二边
$$
L_2L_3^{-1}L_2<\frac12L_1.
$$
因此[原定量 Schur 返回](R271-appendix-quantitative-one-bit-source-transfer-and-six-site-319-over-320.md)
的四项输入可准确取
$$
\varepsilon=\frac23,\qquad
\kappa=\frac13,\qquad
\sigma=\frac12,\qquad
\rho=\frac12.
$$
该稿保留同一 $Qy$、真实第三坐标变分和原 $H_0$，从而给
$$
\Gamma_1\Gamma_2^{-1}\Gamma_1
\preceq\left(1-\frac{\alpha\varepsilon}{2}\right)I,
\qquad
\alpha=\left(1-\frac1{\sqrt3}\right)
       \left(1-\frac1{\sqrt2}\right).
$$
这正是 (1.2) 的首边。

该七位族对取全部倒数权以及共同缩放封闭。
原[倒数权全出生对偶](R239-appendix-primitive-gram-reciprocal-weight-duality-all-births.md)
保留同一源合同，再用其准确相邻反演次序，
把首边预算移到高度三的末边；因此 $j=2$ 也有同一个 $c_*$。

若需要纯有理常数，$1/\sqrt3<29/50$、
$1/\sqrt2<71/100$ 给
$$
\frac{\alpha}{3}>\frac{203}{5000}>\frac1{25}.
$$
因此统一 $24/25$ 也合法；未声称这是该族最优常数。

## 7. 可恢复精确来源与仍未付范围

[可读完整整数源码](../notes/2026-11-28-three-plus-three-joint-source-budget-exact-8542.mjs)
直接从 (3.1) 生成全部五个完整 Gram，按实际度量计算压缩逆，
逐一乘回 (3.7)、(4.1)–(4.3)，再准确展开三条正多项式。
当前 V8 实际返回完整成功，耗时 13 ms；
三条证书分别有 $9$、$11$、$27$ 个严格正系数，
没有使用浮点运算或参数扫描。
只保存证明和可读源码，不另保存可重算数据文件。

这里支付的是指定原有限物理族的联合来源与定量返回。
一般六个独立正权的完整 S1/S2、更高出生的独立权来源、
原无限 carry 与同一 $W$ 的 Green/范围费用仍没有由此完成。
