# R828 — 原四高轴的全精度近顶反射与实际中央 Schur 相容约束

日期：2026-11-15。**状态：以下全精度反射、原 Gaussian 单位消元、原物理四轴的准确运输和同一 Schur 相容式已证明。尚未证明四条原中央条件不相容。**

本篇不把 R821 的四个高轴视作四个可自由指定的算术参数。
它们是同一个原 sigma 的确定系数，且在全部精度下满足一个显示的二维式。
模 $p$ 后，该式进一步由原 $a_p=p\kappa$ 与二次角色 $(2/p)$ 确定。
所有实际低阶卷积、$q_p(2)$、十三行前缀和 native 来源项均保留。

## 1. 原对象与共同好素数

沿用 [R821](R821-original-four-central-axes-and-complete-four-block-carries.md)：
$$
p=6s-1>211,\qquad w=z^6,\qquad
t=-x^{-3},\qquad \Theta=x\sigma^2,\qquad d=1+8t,
\tag{1}
$$
$$
c_p=[w^s]\log(\sigma/z),\qquad
\kappa=34c_p+\Delta,\qquad a_p=p\kappa\in\mathcal O^\times,
\qquad \Delta\in\mathcal O.
\tag{2}
$$
$\mathcal O$ 是原共同 $p$-整系数环。
全部有限坏集仍按 R821，尤其删除
$$
p\mid33226598045199130624.
\tag{3}
$$
以下新增的固定分母素因子均不超过 $23$，已包含于 $p>211$ 的门。
不增加随 $p$ 选择的子式。

原四来源仍是
$$
S=\Theta^{17}f_S,\quad T=\Theta^{36}f_T,\quad
U=\Theta^{68}f_U,\quad V=\Theta^{33}f_V.
\tag{4}
$$
这里 $V$ 是原 $E_{-11}$ 的完整来源，四个 $f_\nu$ 均保持 R821 的固定全多项式。
相对 charge 为
$$
q_S=1,\quad q_T=36/17,\quad q_U=4,\quad q_V=33/17.
\tag{5}
$$

准确的原角展开为
$$
\log\Theta^{17}=\sum_{n\ge1}\ell_nt^n,\qquad
\ell_n=\frac{17}{3n}\frac{(1/3)_n}{(5/6)_n}.
\tag{6}
$$
本文所有近顶系数都来自这个固定展开，未另选一个形式解。

对 $1\le r\le4$，记
$$
A_r^*=\ell_{s-r}
 +(-1)^{s-r+1}\frac{8^{s-r}}{s-r}.
\tag{7}
$$
它正是原 $\log g$ 的 $t^{s-r}$ 系数，其中
$g=d\Theta^{17}e^{-\kappa w^s}$。
Gaussian 从 $t^s$ 才开始，不改变 (7)。

## 2. 全精度近顶反射只含两个原数

定义
$$
R_p=\frac{(1/3)_{s-1}}{(5/6)_{s-1}},\qquad
H_p=\frac{17}{3}(-1)^sR_p,\qquad E_p=8^s,
\tag{8}
$$
及四个固定长度的有理函数
$$
P_r(p)=\prod_{j=1}^{r-1}\frac{p-6j}{p-6j-3},
\qquad P_1=1,\qquad \delta_r(p)=(-8)^rP_r(p).
\tag{9}
$$
所有 $R_p,H_p,E_p,P_r(p)$ 都在 $\mathcal O^\times$。

确实，$R_p$ 的分子、分母因子分别是
$6j-4,6j-1$，其中 $1\le j\le s-1$，没有一个被 $p$ 整除。
(9) 的分子、分母模 $p$ 分别是
$-6j,-6j-3$，在当前范围亦为单位。

由相邻 Pochhammer 比值，对每个 $1\le r\le4$ **在特征零准确有**
$$
\frac{(1/3)_{s-r}}{(5/6)_{s-r}}
 =R_p\prod_{j=1}^{r-1}
 \frac{6(s-j)-1}{6(s-j)-4}
 =R_pP_r(p).
\tag{10}
$$
这里使用 $6s=p+1$；不是只在剩余域中反射。

令
$$
L_r=(-1)^{s-r}A_r^*,\qquad
C_r=8^r(s-r)L_r.
\tag{11}
$$
代入 (7)、(10)，得到本篇的全精度恒等：
$$
\boxed{\quad C_r=H_p\delta_r(p)-E_p,\qquad 1\le r\le4.\quad}
\tag{12}
$$
其中第二项的符号由
$(-1)^{s-r}(-1)^{s-r+1}=-1$ 固定。
没有省略任何 $p$-进位。

因此四个实际高轴处于 (12) 的明确二维线性像中。
这不是说 $H_p,E_p$ 可以自由变化：二者都已经由 (8) 的原有限式确定。

### 2.1 两条准确线性关系与完整恢复

置
$$
D_p^{\rm top}=\delta_2-\delta_1
 =\frac{24(3p-19)}{p-9}.
\tag{13}
$$
其约化为 $152/3$，故在本篇全部素数上为单位。
于是 (12) 等价于两条线性关系
$$
\boxed{
D_p^{\rm top}(C_r-C_1)
 -(\delta_r-\delta_1)(C_2-C_1)=0,
\qquad r=3,4,
}
\tag{14}
$$
连同两个实际参数的恢复式
$$
\boxed{
H_p=\frac{C_2-C_1}{D_p^{\rm top}},\qquad
E_p=\frac{\delta_1C_2-\delta_2C_1}{D_p^{\rm top}}.
}
\tag{15}
$$
式 (14) 是全精度二维约束；式 (15) 还保留原两参数的固定值。
在任意模 $p^j$ 精度中，四个条件 (14)–(15) 均按同一单位分母解释。

### 2.2 $8^s$ 的所有四位不能换成二次角色

令
$$
\chi_2=\left(\frac2p\right)\in\{1,-1\},\qquad
q_p(2)=\frac{2^{p-1}-1}{p}\in\mathbf Z.
$$
因为 $3s=(p+1)/2$，准确有
$$
E_p=2^{(p+1)/2}
 =2\chi_2\sqrt{1+p\,q_p(2)},
\tag{16}
$$
平方根取 $1+p\mathbf Z_p$ 中的唯一一支。
所以
$$
\boxed{
E_p\equiv2\chi_2
 \left(1+\frac p2q_p(2)-\frac{p^2}{8}q_p(2)^2
                  +\frac{p^3}{16}q_p(2)^3\right)\pmod{p^4}.
}
\tag{17}
$$
这是原整数 $8^s$ 的展开。只在模 $p$ 一层才可以写 $E_p=2\chi_2$。

## 3. 同一个超几何单位与原 $a_p$ 的准确关系

先保全低卷积，而后才作模 $p$ 消元。

置
$$
W_0(w)=z^2x(z)=1-\frac w7+\frac{w^2}{637}
                          -\frac{w^3}{84721}+\cdots.
\tag{18}
$$
原恒等式 $\Theta=W_0(\sigma/z)^2$ 给
$$
34c_p=[w^s]\log\Theta^{17}-17[w^s]\log W_0.
\tag{19}
$$
又
$$
p\ell_s=\frac{17(p-3)}{3s}R_p,\qquad
[w^s]t(w)^s=(-1)^s.
$$
因此定义**同一个原低卷积**
$$
\mathcal R_p=
\Delta+\sum_{n=1}^{s-1}
 \ell_n[w^s]t(w)^n-17[w^s]\log W_0(w),
\tag{20}
$$
便有特征零的准确等式
$$
\boxed{
a_p=\frac{p-3}{s}H_p+p\mathcal R_p
    =\frac{6(p-3)}{p+1}H_p+p\mathcal R_p.
}
\tag{21}
$$
特别，
$$
\boxed{
H_p=\frac{p+1}{6(p-3)}(a_p-p\mathcal R_p).
}
\tag{22}
$$

式 (20) 属于 $\mathcal O$：
$\ell_n$ 在 $n<s$ 没有 $p$ 分母；
原 $W_0$、其单位逆以及 $t=-wW_0^{-3}$ 到次数 $s$ 均整；
有限对数只除 $1,\ldots,s$，全为单位。
例如 $W_0$ 的原递推分母是
$(6n+1)(n-1)$，在 $2\le n\le s$ 不含 $p$。
因此 (21) 可合法约化，得
$$
\boxed{H_p\equiv-\frac{a_p}{18}\pmod p.}
\tag{23}
$$

(20)–(22) 也说明为什么不能把 (23) 当成模 $p^4$ 的关系：
高三位仍含原 $\mathcal R_p$，其每一个低 $K$/sigma 卷积均须保留。
本文没有赋 $\mathcal R_p$ 为零，也没有把它当可自由选择的修正。

### 3.1 首共振的阶乘反射核对

同一结论还可以直接用原首共振常数核对。
设
$$
\mathcal C_s=4^{-s}\binom{2s}{s}.
$$
反序 $j\mapsto s-j$ 后，
$$
R_p\equiv
 \prod_{j=1}^{s-1}\frac{2j+1}{2j}
 =\frac{(2s)!}{2^{2s-1}s!(s-1)!}
 =2s\,\mathcal C_s
 \equiv\frac{\mathcal C_s}{3}\pmod p.
\tag{24}
$$
原 [R409](R409-two-actual-sources-shared-first-diagonal-recurrence.md)
的准确首共振为
$$
pc_p\equiv-(-1)^s\mathcal C_s\pmod p.
$$
结合 $a_p\equiv34pc_p$ 得
$$
R_p\equiv-\frac{(-1)^sa_p}{102},\qquad
H_p\equiv-\frac{a_p}{18}.
\tag{25}
$$
故 (23) 与原 Gaussian 的绝对符号一致。
这不是另引一个自由 Hasse 参数。

## 4. 模 $p$ 的四个真实角轴

令
$$
c_r=\prod_{j=1}^{r-1}\frac{2j}{2j+1}
 =1,\ \frac23,\ \frac8{15},\ \frac{16}{35}
 \quad(r=1,2,3,4).
\tag{26}
$$
由 (9)、(23)、(16) 得
$$
C_r\equiv-\frac{a_p}{18}(-8)^rc_r-2\chi_2.
$$
再除 (11) 中的单位，得到
$$
\boxed{
L_r\equiv
 \frac{(-1)^rc_r}{3(6r-1)}a_p
 +\frac{12}{8^r(6r-1)}\chi_2\pmod p.
}
\tag{27}
$$

为明确四个原坐标，(27) 的系数表为：

| $r$ | $a_p$ 的系数 | $\chi_2$ 的系数 |
|---:|---:|---:|
| 1 | $-1/15$ | $3/10$ |
| 2 | $2/99$ | $3/176$ |
| 3 | $-8/765$ | $3/2176$ |
| 4 | $16/2415$ | $3/23552$ |

这是实际 $L_r=(-1)^{s-r}A_r^*$，不是换成独立高轴后的形式 Jacobian。
表中各列有共同来源，但各个 $L_r$ 本身不必为单位。
后文不额外假定某一实际高轴非零。

## 5. 同一物理 $w$ 三角坐标，全尾不删

R821 的物理坐标由
$$
h_A(t)=\sum_{r=1}^4A_rt^{s-r}
      =w^{s-4}P_3(w)+w^sH_A(w),
\qquad P_3=u_0+u_1w+u_2w^2+u_3w^3
\tag{28}
$$
定义。$H_A$ 是真实、确定且线性依赖 $A$ 的完整高尾。

令
$$
T_0(w)=-t/w=W_0^{-3}
      =1+\frac37w+\frac{75}{637}w^2
                       +\frac{2245}{84721}w^3+O(w^4),
\tag{29}
$$
记前三个显示系数为 $\tau_1,\tau_2,\tau_3$，并置 $e_r=s-r$、
$$
b_r=e_r\tau_2+\binom{e_r}{2}\tau_1^2,\qquad
c_4'=e_4\tau_3+e_4(e_4-1)\tau_1\tau_2
                         +\binom{e_4}{3}\tau_1^3.
\tag{30}
$$
式 (29) 由 (18) 的单位逆三次幂直接展开；不需要新增数学数值运行。

按顺序 $\mathbf L=(L_4,L_3,L_2,L_1)^t$，完整的低四阶运输为
$$
\boxed{
\mathbf u=\mathsf T_s\mathbf L,\qquad
\mathsf T_s=
\begin{pmatrix}
1&0&0&0\\
e_4\tau_1&1&0&0\\
b_4&e_3\tau_1&1&0\\
c_4'&b_3&e_2\tau_1&1
\end{pmatrix}.
}
\tag{31}
$$
其行列式为一。
因此对任何 $u\in\mathcal O^4$，都可以先由
$\mathbf L(u)=\mathsf T_s^{-1}u$ 恢复 $L_r(u)$，再定义
$$
C_r(u)=8^r(s-r)L_r(u).
\tag{32}
$$
(14)–(15) 遂成为同一原 $w$ 坐标上的明确整线性条件。

模 $p$ 时，$\mathsf T_s$ 只须取 $s=1/6$。
定义两个固定有理列
$$
\boxed{
v=\mathsf T_{1/6}
 \begin{pmatrix}16/2415\\-8/765\\2/99\\-1/15\end{pmatrix},
\qquad
z=\mathsf T_{1/6}
 \begin{pmatrix}3/23552\\3/2176\\3/176\\3/10\end{pmatrix}.
}
\tag{33}
$$
它们没有 $p$ 依赖；矩阵中的 $\tau_i$ 始终取 (29) 的原有理值。
于是
$$
\boxed{u^*\equiv a_pv+\chi_2z\pmod p.}
\tag{34}
$$
特别 $v_0=16/2415$ 是所有允许素数处的单位。
(33) 本身已经给出各个坐标的有限有理式，不以未执行的数值表作证明。

## 6. 与四条原中央的准确相容检验

保持 R821 的同一参考 $g_\circ$。
令
$$
F_\nu(u)\equiv(a_p/p)J_\nu'(0)\pmod{p^4},
\qquad
b=(F_S(0),F_T(0),F_U(0),F_V(0))^t\bmod p.
\tag{35}
$$
$F_\nu$ 使用原完整八权式及其已经支付的四权化；
$b$ 是那个参考的**实际完整低卷积**，不是自由列。

R821 的固定单位矩阵为
$$
B_4=(A_{\nu,4},A_{\nu,3},A_{\nu,2},A_{\nu,1})_{\nu=S,T,U,V}.
$$
在全部参数点都有
$$
F(u)\equiv b+B_4u\pmod p,
\tag{36}
$$
且唯一模 $p^4$ 的形式 Hensel 解记作 $u^\dagger$。

若四个原完整中央均为零，则原 $u^*$ 必等于 $u^\dagger\bmod p^4$。
因此真实必要条件首先是
$$
\boxed{
b+a_pB_4v+\chi_2B_4z=0\quad\bmod p.
}
\tag{37}
$$
这同时保留原 $a_p$、二次角色和完整 $b$。
没有从 $B_4$ 可逆推出 (37) 自动成立或不可能成立。

例如消去 $a_p$ 后，$u^\dagger\bmod p=-B_4^{-1}b$ 必须满足三条仿射条件
$$
\boxed{
v_0u_i^\dagger-v_iu_0^\dagger
 =\chi_2(v_0z_i-v_iz_0),\qquad i=1,2,3,
}
\tag{38}
$$
而剩余锚定行仍是
$$
u_0^\dagger=a_pv_0+\chi_2z_0.
\tag{39}
$$
这没有把 $a_p$ 消掉后丢弃其真实单位值。

在全四位上，有一个更强且完全准确的检验。
由 $u^\dagger$ 按 (32) 定义 $C_r^\dagger$。
那么
$$
u^\dagger\equiv u^*\pmod{p^4}
$$
**当且仅当**
$$
\begin{cases}
D_p^{\rm top}(C_r^\dagger-C_1^\dagger)
 -(\delta_r-\delta_1)(C_2^\dagger-C_1^\dagger)
       \equiv0\pmod{p^4},&r=3,4,\\[2mm]
(C_2^\dagger-C_1^\dagger)/D_p^{\rm top}
       \equiv H_p\pmod{p^4},\\
(\delta_1C_2^\dagger-\delta_2C_1^\dagger)/D_p^{\rm top}
       \equiv8^s\pmod{p^4}.
\end{cases}
\tag{40}
$$
证明只是 (13) 的单位性、(15) 的完整恢复和 (31) 的整同构。
右边的 $H_p$ 可以用 (8) 的原有限 Pochhammer 积，
也可以用 (22)；若用后者，(20) 不能删除。
最后一行必须使用实际 (17)，不能只代 $2\chi_2$。

(40) 检验的是原四位必要系统与实际 sigma 高轴的相容性，
不是完整中央零的充分条件。
本篇也未证明 (37) 或 (40) 在无穷多个 $p$ 不成立。

## 7. 同一个实际 Bockstein/Schur，而非自由高轴的秩

保 [R824](R824-original-quartic-first-correctors-and-native-central-schur.md)
的同一完整原矩阵。
设 $x\in K_1$ 是一个实际首核，$\Lambda\in C_1^*$ 是其实际首余核左行。
令 $\mathcal L_j$ 为 R821 十二条原末行给出的四个高轴响应。
原等式是
$$
\beta_1(u)(x)=\beta_1^\circ(x)
                 +\sum_{j=0}^3u_j\mathcal L_j(x).
\tag{41}
$$
结合 (34)，真实原来源的 Schur 行准确成为
$$
\boxed{
\Lambda\beta_1^{\rm act}(x)
 =\Lambda\beta_1^\circ(x)
   +a_p\sum_{j=0}^3v_j\Lambda\mathcal L_j(x)
   +\chi_2\sum_{j=0}^3z_j\Lambda\mathcal L_j(x).
}
\tag{42}
$$
若同时使用四个原中央零，亦准确等于
$$
\boxed{
\Lambda\beta_1^\circ(x)
 -\bigl(\Lambda\mathcal L_0(x),\ldots,
          \Lambda\mathcal L_3(x)\bigr)B_4^{-1}b.
}
\tag{43}
$$
(42) 和 (43) 相等所用的正是 (37)，而不是另加一条算术零。

这把原四高轴的超几何依赖实写进同一 native Schur，
没有只说“算术上不独立”而省掉其系数。
它仍不赋 $\Lambda\beta_1^{\rm act}$ 为零或非零；
要排实际提升，须对显示的原项证明相应非零。

全精度也可把 (12)、(31) 逐项代入 R821 的完整 $M_u$。
这只改变参数的书写，以下项目全部保留：

- 三条十三行跨界带与总成本 $39$；
- $w^sH_A$ 的真实高尾及原公共单位；
- $p^3\epsilon^3w^{s-3}P_3^4\mathcal E_{\rm tot}^4/24$ 的末端四次项；
- 原参考及因子提升的 native 差；
- 同一来源格，不把 $V$ 免费加入旧 $Y$ 单部分。

尤其，$M_u\bmod p^4$ 仍只读取 $u\bmod p^3$。
第四位实际相容信息不能仅因是额外一位，就被计为新的深核。

## 8. 四个首必要系数的准确范围

令
$$
\alpha_\nu=[w^s]\nu=[z^{p+1}]\nu.
$$
原四来源质量为零、首阶为 $w$，故删 Gaussian 不改变此系数。
R821 的整四权式给
$$
J_\nu'(0)=0\quad\Longrightarrow\quad
\alpha_\nu=0\pmod p.
\tag{44}
$$
本篇的 (37) 是这四个真实必要行在原高轴分离后的准确式。

不同 charge 的完整 $K$ 卷积仍包含在 $b$ 和 (20) 中。
它们不能只因四个近顶系数共用 $H_p$，就被认作同一个自由余项或删去。
同样，原 $S(mz)/m^6$ 的倍点来源仍受 R821/R824 的完整 native 拉回恒等约束；
本篇没有把其形式低 jet 独立重复计成新中央条件。

后续真正需要判定的是 (37)/(40) 对这批实际低卷积的值，
或 (42) 对同一真实首核/左行的值。
固定反射、单位 Jacobian、共同迹域和非零时的高度上界，
各自都不替代这个指定非零问题。

本篇全部证明为符号恒等与原整性论证。
没有新增目标素数扫描、数值运行或可重算输出文件。
