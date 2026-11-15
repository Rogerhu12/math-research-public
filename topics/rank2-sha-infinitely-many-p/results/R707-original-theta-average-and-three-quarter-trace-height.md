# R707 — 原固定 theta 全迹的三分之四高度界

日期：2026-11-15。**状态：以下原全 Hall 迹的复平方平均、
固定分母高度界及非零边界的严格小于一估值上界已证明。
本篇不证明原迹非零，也不另行假定原中央条件给出边界零。**

本篇使用 R704 的原固定 theta 高斯展开和 R705 的绝对 Weil 模型。
所得收益是对原迹全部复共轭的真实平方平均，
不需要对每一个小矩形或短块先证明最大值节省。
整个 Hall 群、原 theta 系数、非单位向量以及固定分母均保留。

## 1. 原来源与目标

保持
$$
p=6s-1>101,\quad q=p^2,\quad d=p+1,\quad
m\in\{34,72\},\quad R=\mathbf Z[\omega]/q.
$$
$N(a+b\omega)=a^2-ab+b^2$。
原复 theta 样本为
$$
A_m(v)=\mathfrak k(\Omega v/p)^m\phi_m(T_v)\in\mathcal V_m.
$$
它在 $v=0\bmod p$ 按原零阶 6 延拓，所以 $A_m(0)=0$。
R703–R705 的原和为
$$
\mathscr S_{p,m}(r)=\langle A_m,G_r\rangle,
\qquad r\in\mathbf F_p^\times,
$$
其中 $\|G_r\|^2=d$，$\chi_{m,r}$ 为已经付清的原 wild 角色。
原代数迹满足
$$
|\mathcal T_{m,T_v}|=|\mathscr S_{p,m}(Nv)|.
\tag{1}
$$

将证明存在仅依固定原来源的常数 $C_m$，使
$$
\boxed{
\sum_{r\in\mathbf F_p^\times}
 |\mathscr S_{p,m}(r)|^2
 \le C_m p^{5/2}(1+\log p)^{3/2}.
}
\tag{2}
$$
因此全部 $r$ 的均方根为
$O_m(p^{3/4}(1+\log p)^{3/4})$。
这是平均界，不是对每个 $r$ 的同一上确界。

## 2. 同一原样本的固定高斯包

令 $\mathcal Z:\mathcal V_m\to\mathbf C^{\mathbf Z/q}$ 为
R704/R706 的实际逆 Zak，
并定义
$$
f_{m,p}=\frac{\mathcal ZA_m}{p}.
\tag{3}
$$
R704 的磁全纯方程及原准周期给有限个固定复常数
$d_0,\ldots,d_{m-1}$，使
$$
\boxed{
f_{m,p}(n)
=q^{-1/4}\sum_{k\in\mathbf Z}
 d_{[pk\bmod m]}
 \exp\!\left[
 -\pi m\tau\,\frac{(n-qk/m)^2}{q}\right],
\quad
\tau=\frac{\sqrt3-i}{2}.
}
\tag{4}
$$
这里 $p$ 只置换这 $m$ 个固定系数。
(4) 在 $n\bmod q$ 周期。
按 $k=j+m\ell$ 分组，它是 $m$ 个固定宽度参数、
中心在 $qj/m$ 的周期高斯包的和。
原 $\phi_m$、周期及全部 theta 系数均在这些固定 $d_j$ 中；
未把原来源换成一个任选高斯。

特别地，
$$
\|f_{m,p}\|_2\le C_m.
\tag{5}
$$
以下允许这个范数不为 1。
所有常数只依 $m$、这批固定 $d_j$ 和原周期，不依 $p$。

## 3. 原高斯包的完整 Heisenberg 重叠界

仍用 R706 的
$$
(\mathsf D_{(x,y)}f)(n)
=e_q(-my(n+x/2))f(n+x).
$$
对 $c>0$ 定义二维周期高斯
$$
\Gamma_{q,c}(u)
=\sum_{\substack{U\in\mathbf Z[\omega]\\U\equiv u\bmod q}}
                 \exp(-cN(U)/q).
\tag{6}
$$
存在固定 $c_m,C_m>0$，使对全部 $t=x+y\omega\in R$，
$$
\boxed{
|\langle f_{m,p},\mathsf D_t f_{m,p}\rangle|
 \le C_m\,\Gamma_{q,c_m}(mt).
}
\tag{7}
$$
$m$ 在 $R$ 中可逆；这个乘法不是将原输入另换为自由坐标。

### 完成平方与 Poisson 求和的全细节

先取一个未平移高斯
$q^{-1/4}\exp(-\pi m\tau n^2/q)$。
它与 (3) 的 Heisenberg 平移重叠后，
令 $u=n+x/2$，指数中的实衰减与线性相位准确为
$$
-\frac{\pi m\sqrt3}{q}u^2
-\frac{\pi m\sqrt3}{4q}x^2
+\frac{2\pi i m}{q}(y-x/2)u.
$$
对整数 $n$ 作一维 Gaussian Poisson 求和，
取绝对值后由
$$
\frac{\pi m\sqrt3}{4q}x^2+
 \frac{\pi}{m\sqrt3 q}(my-mx/2-qb)^2
 =
\frac{\pi}{m\sqrt3 q}
 N\bigl(mx+(my-qb)\omega\bigr)
\tag{8}
$$
控制，$b\in\mathbf Z$。
常数因子为固定的 $(m\sqrt3)^{-1/2}$。

对两个周期包，先把 $\sum_{n\bmod q}$ 与其中一个周期指标展开为
$\sum_{n\in\mathbf Z}$；另一个周期指标把 $x$ 换成 $x+q\ell$。
若两包中心分别为 $qj/m,qk/m$，
则还把 $x$ 换成
$$
x+q(j-k)/m+q\ell.
$$
乘上 $m$ 后，这些第一坐标全在 $mx+q\mathbf Z$ 内。
中心引入的剩余因子模为一，不能增大 (8)。
把有限个 $j,k$、固定系数和全部周期指标一起求和，
即得 (7)，例如可以取 (8) 所示
$c_m=\pi/(\sqrt3m)$，再增大固定 $C_m$。

这一证明保留全部交叉包，
没有只估一个包或只估原短块的一部分。

## 4. 全空间 Weyl 正交性

$\mathscr H=\mathbf C^{\mathbf Z/q}$ 的维数为 $q$。
$R$ 中的 $q^2$ 个 $\mathsf D_t$ 满足
$$
\operatorname{Tr}(\mathsf D_t\mathsf D_u^*)=q\,\mathbf1_{t=u}.
\tag{9}
$$
对 $f=f_{m,p}$ 置
$$
a_f(t)=\langle f,\mathsf D_t f\rangle,\qquad
c_f(h)=\langle f,\mathsf W(h)f\rangle.
$$
把秩一算子 $|f\rangle\langle f|$ 在 (9) 中展开，
并用完整交织
$\mathsf W(h)\mathsf D_t\mathsf W(h)^{-1}=\mathsf D_{ht}$，得到
$$
\boxed{
|c_f(h)|^2
 =\frac1q\sum_{t\in R}
        a_f(t)\overline{a_f(h^{-1}t)}.
}
\tag{10}
$$
这是真正的全空间恒等。
它不把一个完整相关函数当作某个短区间内的相关函数。

令 $\widehat H$ 为 R703 的阶 $d$ Hall 群。
由 (7)、(10)，
$$
\sum_{h\in\widehat H}|c_f(h)|^2
 \le\frac{C_m}{q}
 \sum_{\substack{h\in\widehat H\\t\in R}}
 \Gamma_{q,c_m}(mt)\Gamma_{q,c_m}(mh^{-1}t).
\tag{11}
$$
$m$ 与 $h$ 交换且在 $R$ 中可逆，
所以右端可严格用 $u=mt$ 重标。

## 5. 单位向量的实际范数同余计数

先限制 $u\in R^\times$。
给定 $u,w\in R^\times$，方程 $w=h^{-1}u$ 至多确定一个
$h\in\widehat H$。
又真正 Hall 提升满足 $Nh=1\bmod q$。
故该部分不超过
$$
\sum_{\substack{u,w\in R^\times\\Nu=Nw\bmod q}}
       \Gamma_{q,c_m}(u)\Gamma_{q,c_m}(w).
\tag{12}
$$
没有把 $\widehat H$ 改成只在模 $p$ 范数为一的任选提升；
(12) 只是对其实际像取了一个更大的上界集合。

把 (6) 的所有整数提升展开，(12) 不超过
$$
\mathscr N_q=
\sum_{\substack{U,V\in\mathbf Z[\omega]\\
                N(U)\equiv N(V)\bmod q}}
      \exp[-c_m(N(U)+N(V))/q].
\tag{13}
$$
下面的初等估计足够：
$$
\boxed{\mathscr N_q\le C_m q(1+\log q)^3.}
\tag{14}
$$

为证明它，记
$$
R_E(n)=\#\{U\in\mathbf Z[\omega]:N(U)=n\}.
$$
$R_E(0)=1$。
Eisenstein 整数的唯一分解给
$R_E(n)\le6\,\mathrm d(n)$：
分裂素数的指数 $a$ 至多有 $a+1$ 种分配，
惰性和分歧素数不增加此上界，最后乘六个单位。
逐素数有 $\mathrm d(n)^2\le\mathrm d_4(n)$，
而
$$
\sum_{n\le X}\mathrm d_4(n)
 \le X(1+\log X)^3.
$$
因而
$$
\sum_{0\le n\le X}R_E(n)^2
 \le C X(1+\log X)^3.
\tag{15}
$$

在 (13) 中把 $N(U),N(V)$ 分别分到
$[aq,(a+1)q)$、$[bq,(b+1)q)$。
同余配对的和由 Cauchy–Schwarz 及 (15) 控制为
$$
Cq\sqrt{(a+1)(b+1)}
 (1+\log((a+1)q))^{3/2}
 (1+\log((b+1)q))^{3/2}.
$$
乘上 $e^{-c_m(a+b)}$ 后对 $a,b\ge0$ 求和，
固定指数衰减吸收所有 $a,b$ 因子，得到 (14)。

这里的同余是模 $q=p^2$，不是模 $p$；
这正是得到所需计数大小的地方。

## 6. 非单位向量与零向量不能省略

对 $u=pu_0\ne0$，$u_0\in\mathbf F_{p^2}^\times$，
由 (6)
$$
\Gamma_{q,c_m}(pu_0)
 =\sum_{\substack{U_0\in\mathbf Z[\omega]\\
                  U_0\equiv u_0\bmod p}}
                      e^{-c_mN(U_0)}.
\tag{16}
$$
把 (16) 对全部 $u_0$ 求和是一个固定收敛的二维 Gaussian 和。

$\widehat H$ 在非零 $u_0$ 上自由作用。
因此对每个 $u_0\ne0$，
$$
\sum_{h\in\widehat H}\Gamma_{q,c_m}(ph^{-1}u_0)
 \le\sum_{w_0\in\mathbf F_{p^2}}
             \Gamma_{q,c_m}(pw_0)
 \le C_m.
$$
再乘 (16) 并求和，全部非零非单位的贡献为 $O_m(1)$。

这里必须保留 $\widehat H$：
若免费扩为全 $p^2$ 范数一群，其主单位核会产生额外 $p$ 重数。
本证明没有这样做。

最后 $u=0$ 由全部 $d$ 个 Hall 元固定，
其贡献为 $d\Gamma_{q,c_m}(0)^2=O_m(d)$。
所以 (11)–(16) 严格给
$$
\boxed{
\sum_{h\in\widehat H}
 |\langle f_{m,p},\mathsf W(h)f_{m,p}\rangle|^2
 \le C_m(1+\log p)^3.
}
\tag{17}
$$
零向量的 $O(d/q)=O(p^{-1})$ 已包含在此界内。

## 7. 原 Hall 投影的实际平均收益

令
$$
\mathsf P_H=\frac1d\sum_{h\in\widehat H}\mathsf W(h).
$$
这是正交投影，故
$$
\|\mathsf P_Hf_{m,p}\|^2
 =\frac1d\sum_{h\in\widehat H}
             \langle f_{m,p},\mathsf W(h)f_{m,p}\rangle.
$$
对这整个和使用 Cauchy–Schwarz 和 (17)，得
$$
\boxed{
\|\mathsf P_Hf_{m,p}\|^2
 \le C_m d^{-1/2}(1+\log p)^{3/2}.
}
\tag{18}
$$

R705 的完整 torus 分解表明，
Hall 不变空间由旧一维向量及
$G_r/\sqrt d$（$r\ne0$）组成。
原 $A_m(0)=0$，因此旧一维分量严格为零，而不是被省略。
由 (3) 的真实归一，准确有
$$
\boxed{
\sum_{r\ne0}|\mathscr S_{p,m}(r)|^2
 =d\,\|\mathsf P_HA_m\|^2
 =dp^2\|\mathsf P_Hf_{m,p}\|^2.
}
\tag{19}
$$
把 (18) 代入即得 (2)。

这里的 $p^2$ 是原样本与归一高斯包之间的实际范数因子。
若把它删掉，会得到一个错误的更强界。
本篇保留该因子后仍获得严格的四分之一次幂节省。

## 8. 全部绝对嵌入的均匀 r 分布

置
$$
E_W=W^{\widehat H}.
$$
R696/R705 给
$$
[E_W:K_0]=p(p-1),
$$
且 $E_W$ 在有理素数 $p$ 上只有一个位，
该位的绝对局部次数等于全局次数。

对 $\operatorname{Gal}(W/K_0)$ 中的 $g$，
$g(w_v)$ 是原 $a_{T_{gv}}$ 的一个 $p$ 次根。
它与 R703 所选 $w_{gv}$ 只相差 $\mu_p$ 中的根单位。
该根单位由 Hall 群固定，故可提出原迹。
于是 (1) 在 Galois 运输后保持，
绝对值只按 $r=N(gv)\bmod p$ 变化。

范数
$\mathbf F_{p^2}^\times\to\mathbf F_p^\times$ 满射，
并且 Hall 商恰由该范数标记。
主单位的 $p$ 个共轭按 R705(17) 只乘模一根单位。
因此在 $E_W/K_0$ 的全部嵌入中，
每个 $r\ne0$ 的绝对值 $|\mathscr S_{p,m}(r)|$
准确出现 $p$ 次。

$K_0$ 的另一个复嵌入也必须保留：
原曲线 $b=17$ 和 $\phi_m$ 为实系数，
共轭将 $\omega$ 换成 $\omega^2$，
将原 Klein 相位及 wild 角色同时共轭。
范数 $r$ 不变，绝对值仍为同一组数。
所以对全部绝对嵌入，
$$
\boxed{
\frac1{[E_W:\mathbf Q]}
 \sum_\sigma\log^+|\sigma(\mathcal T_{m,T_v})|
 =
 \frac1{p-1}\sum_{r\ne0}\log^+|\mathscr S_{p,m}(r)|.
}
\tag{20}
$$
即使该迹位于 $E_W$ 的真子域，(20) 也可在 $E_W$
中按重数计算，不能因此删除某些共轭。

## 9. 固定分母高度及非零边界的严格估值界

R700 已给固定整数
$$
D_m=
7\,2^{\lceil m/3\rceil}
  3^{\lceil m/4\rceil}
  17^{\lceil m/6\rceil}
$$
使 $D_m\mathcal T_{m,T_v}$ 在全部有限位整。
结合 (2)、(20) 与 Jensen，
$$
\begin{aligned}
\frac1{p-1}\sum_{r\ne0}\log^+|\mathscr S_{p,m}(r)|
&\le\frac12\log\left(
 1+\frac1{p-1}\sum_{r\ne0}|\mathscr S_{p,m}(r)|^2\right)\\
&\le\frac34\log p+
       \frac34\log(1+\log p)+O_m(1).
\end{aligned}
$$
有限分母只贡献固定的 $\log D_m$。
因此
$$
\boxed{
h(\mathcal T_{m,T_v})
 \le\frac34\log p+
       \frac34\log(1+\log p)+O_m(1).
}
\tag{21}
$$
这是对原同一个代数迹的高度界，
不需要每个复共轭的单独最大值节省。

若该迹非零，取 $D_m\mathcal T$ 的绝对整数范数。
唯一 $p$ 位的次数权重为 1，
而其他有限位的整性不能抵消该 $p$ 因子。
于是
$$
\boxed{
v_p(\mathcal T_{m,T_v})
 \le\frac34+
   \frac{\frac34\log(1+\log p)+O_m(1)}{\log p}.
}
\tag{22}
$$
这里 $p\nmid D_m$。
也可以直接对非零整数范数的全部复绝对值使用
(2) 的均方界，得到同一结论。

R696 的原边界恒等仍为
$$
v_p(\mathcal T_{m,T_v})
 =\frac1{p-1}+v_p(\mathcal B_m(v_T^d)).
$$
所以对于非零原边界，
$$
\boxed{
v_p(\mathcal B_m(v_T^d))
 \le\frac34+
   \frac{\frac34\log(1+\log p)+O_m(1)}{\log p}
   -\frac1{p-1}.
}
\tag{23}
$$
特别地，存在只依固定原来源的门 $p_0(m)$，
使所有 $p>p_0(m)$ 的非零原边界均满足
$$
\boxed{v_p(\mathcal B_m(v_T^d))<1.}
\tag{24}
$$
因此若另由原算术或同一实际来源证明该边界的估值至少为 1，
则这个边界必须为零。
(24) 本身没有断言原边界非零，
也没有替代原完整 $j_m=0$ 与边界之间尚需的实际关系。

## 10. 与前沿的准确关系

R700 的逐项复界给高度主系数 1；
本篇使用原固定 theta 的磁全纯高斯结构，
把同一个迹的高度主系数严格降到 $3/4$。
关键新增输入是 (7) 的完整高斯 Heisenberg 界，
以及模 $p^2$、保非单位的范数同余计数。

以下内容均没有被假定：

- 原小 section 指数和的统一平方根上界；
- 将全相关等同于短块内相关；
- 任意改变 Hall 的 $p^2$ 提升；
- 从局部投影或一个正矩推出原中央非零；
- 删除 $K_0$ 的共轭或零向量；
- 将 $f_{m,p}$ 当作与原来源无关的任选向量。

原完整来源、实际角色、全部共轭与固定分母已在同一条链中保齐。
后续应把 (23)–(24) 与原 $j_m$ 给出的真正边界条件联立，
而不是再添加一条独立的中央零。

## 依赖

- R704：原固定 theta 的磁全纯 Fourier/高斯展开及绝对 Zak 规范。
- [R705](R705-original-wild-character-and-absolute-weil-projection.md)：
  原角色、整个有限 Weil 模型、单重 torus 分解及 $W/F$ 恰为 $p$。
- [R706](R706-original-bessel-kernel-and-complete-stationary-fibres.md)：
  同一 Schrödinger 规范与完整例外。
- [R700](R700-original-fixed-denominator-and-logarithmic-trace-height.md)：
  原固定分母、全部绝对嵌入及唯一 $p$ 位。
- [R696](R696-original-absolute-roots-p2-field-and-linear-height-trace.md)：
  同一原迹与边界恒等。

本篇为一般证明，没有数值扫描或新增可重算数据文件。
