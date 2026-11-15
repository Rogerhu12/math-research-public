# R762 — 穿过原 S 的真实正交 Cayley 家族、非零中央横向导数与 ordinary-core 修正

日期：2026-11-15。**状态：已证明。** 本篇从原固定来源的准确分解 $S=\sigma(S/\sigma)$ 构造一条真实 norm-preserving 家族，证明其原 unit 中央导数在 $u=0$ 的横向导数非零。若原 $J'_S(0)=0$，它在这条家族中是一个简单的 $u$ 零点。

结论不把附近来源认作同一个固定 Katz 角色或同一 ordinary 特征向量。相反，第 6 节给出一个准确而非零的 ordinary-core 交换修正。所有正权、原单位切割、$\Omega_p,d_p$、尺度质量项及 higher jet 均保持。

## 1. 同一原 sigma 的完整两输入来源

沿用 R728、R759、R761 的原规范，固定
$$
b=17,\qquad H=S/\sigma,\qquad
D_S=\zeta S-\frac1{34}S',\qquad
\Omega=\Omega_p,\quad d_p=p-1.
\tag{1}
$$
S 首项为 $z^6$，故 H 首项为 $z^5$，是原标准 odd degree33 的全纯截面。
它不是另选的 rank-one 来源。

取实际有界联合测度
$$
\mu=\nu_\sigma(c)\otimes\nu_H(v).
\tag{2}
$$
原变换规范为
$$
\int e^{xz/\Omega}\,d\nu_F(x)=F(z).
\tag{3}
$$
定义两个物理观察
$$
Y=c+v,\qquad
Z=c-\frac{Y}{34}=\frac{33c-v}{34}.
\tag{4}
$$
原两个输入的 Hermitian 范数为1及33；因此
$$
\langle Y,Z\rangle=0,\qquad
\|Y\|^2=34,\qquad
\|Z\|^2=\frac{33}{34}.
\tag{5}
$$
其完整联合生成函数准确为
$$
\begin{aligned}
F(z,w)
&=\int\exp((Yz+Zw)/\Omega)\,d\mu\\
&=\sigma\left(z+\frac{33}{34}w\right)
  H\left(z-\frac1{34}w\right).
\end{aligned}
\tag{6}
$$
故
$$
F(z,0)=S(z),\qquad
\boxed{\partial_wF(z,0)=D_S(z).}
\tag{7}
$$
(7) 由
$\frac{33}{34}\sigma'H-\frac1{34}\sigma H'
 =\zeta S-S'/34$
直接得到，保留了原连接中的 $\sigma'H$。

这里 first-Y 的自动因子不依赖 w：两个输入的交叉系数
$33/34+33(-1/34)$ 为零。把伙伴变量写成 $w=34w_0$ 后，(6) 是实际
$S_{34}\otimes S_{1122}$ 联合 theta 截面，且保原两 odd 半特征。
于是每个
$$
D_j(z):=\partial_w^jF(z,0)
\tag{8}
$$
都为原标准 degree34 截面；$D_0=S,D_1=D_S$。
这不表示沿一个变动斜对角得到的来源仍在同一个一变量标准格。

由 (3)、(6)，完整测度身份是
$$
\boxed{
\nu_{D_j}=\Omega^{-j}Y_*(Z^j\mu).
}
\tag{9}
$$
它保留了原两个输入，而不是给裸边际重新添一个无关伙伴。

## 2. 真正正交 Cayley 族及全部正权

置
$$
r=\frac{\|Z\|^2}{\|Y\|^2}=\frac{33}{1156},
$$
$$
a(u)=\frac{1-r u^2/4}{1+r u^2/4},\qquad
b(u)=\frac{u}{1+r u^2/4}.
\tag{10}
$$
定义
$$
Y_u=a(u)Y+b(u)Z,\qquad
Z_u=-r b(u)Y+a(u)Z.
\tag{11}
$$
恒等式 $a(u)^2+r b(u)^2=1$ 说明 (11) 保持 (5) 的整个 Gram 矩阵。
在 $u=0$，
$$
\dot Y_0=Z,\qquad \ddot Y_0=-rY,\qquad
\dot a(0)=0,\quad \dot b(0)=1.
\tag{12}
$$
没有用线性剪切替代这个实际 norm-preserving 族。

其第一来源是
$$
\begin{aligned}
A_u(z)
&=(Y_u)_*\mu\ \text{的变换}\\
&=F(a(u)z,b(u)z)\\
&=\sigma\left(\left(a+\frac{33}{34}b\right)z\right)
  H\left(\left(a-\frac1{34}b\right)z\right).
\end{aligned}
\tag{13}
$$
原两输入参数的平方范数和恰为34；原来源在 $u=0$ 正好是 S，不是其倍数。

对每个整数 $n\ge0$，全部正矩为
$$
\boxed{
M_n(u)=\int Y_u^n\,d\mu
 =\sum_{j=0}^n\binom nj a(u)^{n-j}b(u)^j
                 \int Y^{n-j}Z^j\,d\mu
 =\Omega^n n![z^n]A_u(z).
}
\tag{14}
$$
全部角权都保留。原联合类型为0，所以
$M_n(u)=0$ 当 $n\not\equiv0\bmod6$；这来自整个 (6) 的同时旋转，
不是对某个独立 Fourier 分支作删除。

一阶式在所有正权为
$$
\boxed{
M_n'(0)=n\Omega\int Y^{n-1}\,d\nu_{D_S}(Y)
       =\Omega^n n![z^{n-1}]D_S .
}
\tag{15}
$$
$n=0$ 时左右均取零。完整第二阶为
$$
M_n''(0)
=n(n-1)\Omega^2\int Y^{n-2}\,d\nu_{D_2}
 -nr\int Y^n\,d\nu_S .
\tag{16}
$$
第二项是实际 Cayley 尺度补偿，不因正交性而省略。

所有 higher derivatives 可由下面的完整生成式读取：
$$
A_u(z)=
 \sum_{j\ge0}\frac{b(u)^jz^j}{j!}D_j(a(u)z).
\tag{17}
$$
这里同时保留 $a(u)$ 的全部阶；不能只保 $z^jD_j$。

## 3. 原 p-adic 单位切割严格不动，质量保持零

固定原好 ordinary p，特别 $p\nmid2\cdot3\cdot17$。
原 (2) 支撑在 $\mathbf Z_p^2$，(4) 的34为单位。
对整个 $u\in p\mathbf Z_p$，
$$
a(u)\equiv1\bmod p,\qquad b(u)\equiv0\bmod p,
$$
所以点对点准确有
$$
\boxed{
Y_u\ {\rm unit}\ \Longleftrightarrow\ Y\ {\rm unit},
\qquad
Y_u\in p\ \Longleftrightarrow\ Y\in p.
}
\tag{18}
$$
本篇只用这个原一层 unit 切割；没有宣称任意原 mixed W/E 深门也固定。

因此定义真实完整 Mellin 族
$$
\mathcal M(u,s)=
 \int_{\{Y\ {\rm unit}\}}\langle Y_u\rangle^{d_ps}\,d\mu .
\tag{19}
$$
它在 $u\in p\mathbf Z_p$ 与原 s 权圆盘上联合解析。证明是
$Y_u/Y\in1+p\mathbf Z_p$，其主单位 logarithm 和指数在整个固定紧域上一致收敛；有界测度允许逐阶积分。
Teichmüller 因子不随 u 变化。

原整个 S34 偶核为
$\nu_S|_p=\lambda[\kappa]_*\nu_S$，且 $S(0)=0$。
于是
$$
\boxed{
\mathcal M(u,0)=\nu_S(\mathbf Z_p^\times)
 =(1-\lambda)S(0)=0
 \quad\text{对全部 }u\in p\mathbf Z_p.
}
\tag{20}
$$
这是真正固定 unit 域的质量，不从 $A_u(0)=0$ 单独推断。

令
$$
\mathcal J(u)=\partial_s\mathcal M(u,0),\qquad
\mathcal J(0)=J_S'(0).
\tag{21}
$$
这里 $u$ 是空间方向，$s$ 是原 Mellin 权；二者没有互换。

## 4. 全 Mellin first jet 与非零横向导数

定义带原周期的完整负一行
$$
\mathbb I_{D_S}(s)=
\Omega\int_{Y\ {\rm unit}}
      Y^{-1}\langle Y\rangle^{d_ps}\,d\nu_{D_S}(Y).
\tag{22}
$$
对 (19) 的实际观察求导，用 (9)、(12)，得到整条函数等式
$$
\boxed{
\partial_u\mathcal M(0,s)=d_ps\,\mathbb I_{D_S}(s).
}
\tag{23}
$$
所以
$$
\boxed{
\mathcal J'(0)
 =d_p\mathbb I_{D_S}(0)
 =d_p\Omega\int_{Y\ {\rm unit}}Y^{-1}\,d\nu_{D_S}\ne0.
}
\tag{24}
$$
非零是 R761 公开增补的完整 point-field 结论：
$$
e_2^{\log}\mathbb I_{D_S}(0)
 =\frac{11}{21}\mathbb I_{D_\omega}(0)\ne0.
\tag{25}
$$
R761 的三个 primitive 九阶 sector、代数系数和原 period 全部已经纳入 (25)；
没有用首 $z^5$ 系数代替负一矩非零。
$d_p=p-1$ 是单位，$\Omega\ne0$，也没有约去一个未知零因子。

更一般地，对每个整数 $k\ge1$，
$$
\partial_u\partial_s^k\mathcal M(0,0)
 =k\,d_p\,\mathbb I_{D_S}^{(k-1)}(0).
\tag{26}
$$
$k\ge2$ 的负一 logarithm 导数仍保未知，不由 (25) 的 finite point projector推出其值。

为明确第二阶的完整权补偿，置
$$
\mathbb I_{D_2,-2}(s)=
 \Omega^2\int_{Y\ {\rm unit}}
       Y^{-2}\langle Y\rangle^{d_ps}\,d\nu_{D_2}.
$$
则
$$
\boxed{
\partial_u^2\mathcal M(0,s)
=d_ps\bigl((d_ps-1)\mathbb I_{D_2,-2}(s)
                 -r\,\mathcal M(0,s)\bigr).
}
\tag{27}
$$
这同时显示 falling-factorial 权与 Cayley 的尺度项。只有在对指定阶代入已证质量关系后，才能消去相应质量；不能先从公式删去它。

本篇权为固定的1，故没有隐藏的 moving polynomial 权项。
若另乘随 u 变化的 $f_u$，完整一阶必须另加
$J'_{\dot f_0}(0)$；若观察再乘 $h(u)$，还须另加
$d_p h'(0)h(0)^{-1}\mathcal M_f(0,0)$。
这些正是原剪切 note 的完整项，本篇不把其零性推广到原其他门。

## 5. 真正 simple u-zero 与全部高阶余项

在 Y-unit 上有
$$
Y_u/Y=a(u)\bigl(1+t(u)Z/Y\bigr),\qquad
t(u)=b(u)/a(u)=\frac{u}{1-r u^2/4}.
$$
固定 unit 质量 (20) 准确消去 $\log\langle a(u)\rangle$ 的项。于是
$$
\boxed{
\mathcal J(u)=J_S'(0)
 +d_p\sum_{j\ge1}\frac{(-1)^{j+1}}j\,
          t(u)^j
          \int_{\{Y\ {\rm unit}\}}(Z/Y)^j\,d\mu .
}
\tag{28}
$$
若用 (9)，第 j 项的积分就是
$\Omega^j\int_{Y\ {\rm unit}}Y^{-j}d\nu_{D_j}$。
这是整个实际来源的收敛负矩级数；不对这个无限和施加 R749 的有限 point-factor projector。

由 (24)，在任一原好 ordinary p：
$$
\boxed{
J_S'(0)=0
 \quad\Longrightarrow\quad
u=0\text{ 是 }\mathcal J(u)\text{ 的简单零点}.
}
\tag{29}
$$
因此存在该 p 的一个真邻域，使全部非零 u 均满足
$\mathcal J(u)\ne0$。这不是说原 $u=0$ 值非零。

还能保一个准确的赋值门。取整数 $B_p\ge0$ 使
$p^{B_p}\mu$ 为整有界测度，置
$$
v_p(d_p\mathbb I_{D_S}(0))=t_p.
$$
对于 $u\ne0$、$v_p(u)=q\ge1$ 且
$$
q>B_p+t_p,
\tag{30}
$$
(28) 的所有 $j\ge2$ 项赋值至少 $2q-B_p$。
理由是 $Z/Y$ 整，$v_p(t(u))=q$，且
$j q-v_p(j)\ge2q$ 对 $j\ge2$ 成立。
所以在 (29) 的假设下
$$
\boxed{v_p(\mathcal J(u))=q+t_p.}
\tag{31}
$$
$B_p,t_p$ 均对应原 p 与原来源；没有宣称它们对 p 一致，或可选一个对无穷 p 同时足够小的固定非零有理 u。

## 6. ordinary-core 不能在这个族上冻结

这一节给出同一原有限来源的另一条确切检查。记
$$
A_u^{\rm deep}(z)
 =\int_{\{Y\in p\}}e^{Y_u z/\Omega}\,d\mu,\qquad
A_u^\times=A_u-A_u^{\rm deep}.
\tag{32}
$$
域由 (18) 完整固定。在 $u=0$，
$$
A_0^{\rm deep}=\lambda S(\kappa z),\qquad
A_0^\times=S(z)-\lambda S(\kappa z).
\tag{33}
$$
但对 u 求导时，(9) 及原 odd S34 核
$\nu_{D_S}|_p=\beta[\kappa]_*\nu_{D_S}$，$\beta=-\lambda$，
准确给
$$
\boxed{
\left.\partial_uA_u^{\rm deep}(z)\right|_0
 =\beta zD_S(\kappa z),\qquad
\left.\partial_uA_u^\times(z)\right|_0
 =zD_S(z)-\beta zD_S(\kappa z).
}
\tag{34}
$$
另一方面，若无证将整族都当作同一 even ordinary 特征向量，
$\lambda A_u(\kappa z)$ 的导数会是
$\lambda\kappa zD_S(\kappa z)$。
两者的准确差为
$$
\boxed{
\left.\partial_u
 \bigl(A_u^{\rm deep}(z)-\lambda A_u(\kappa z)\bigr)\right|_0
 =(\beta-\lambda\kappa)zD_S(\kappa z)\ne0.
}
\tag{35}
$$
因为 $\beta=-\lambda$、$v_p(\kappa)=1$，系数
$\beta-\lambda\kappa=-\lambda(1+\kappa)$ 非零；
$D_S$ 也非零。因此整个邻域不能满足那个固定 ordinary-core 身份。

按所有正权写出相同差，(34) 给
$$
\boxed{
\left.\partial_u\right|_0
 \int_{\{Y\ {\rm unit}\}}Y_u^n\,d\mu
 =n\Omega(1-\beta\kappa^{n-1})
        \int Y^{n-1}\,d\nu_{D_S}.
}
\tag{36}
$$
它不是把 $(1-\lambda\kappa^n)$ 乘到 (15) 上。两个 Euler 形状的区别恰由 (35) 支付。
$n=0$ 仍按质量为零解释，不能将 $\kappa^{-1}$ 因子单独取出。

## 7. 对原 fixed-representation 门的精确意义

(6) 是固定的真实两变量 theta 截面；(13) 是其实际斜限制。
这不把所有 $A_u$ 自动放入同一个一变量标准 S34 空间。
事实上 first jet 是 $zD_S$，其非零周期差已经由原剪切 note 支付；(35) 进一步排除同一原 ordinary eigline 在该族上保持不变。

这些结论没有排除另一个完整 automorphic 实现。
若要用原 $J'_S(0)=0$ 强迫所有 $\mathcal J(u)=0$，仍需证明原剪切 note 的 fixed-$L_p$ 身份，包括同一全局表示、坏处角色、周期、实际 p-local vector 与非零 local pairing。
不能因 (5) 的范数相同就断言该身份成立。

若这样一个完整同源单位因子身份成立，(24)、(29) 将给直接矛盾；
但本篇没有假定它。已支付的实际进展是：原 S 上一条明确、完整、保原 unit 域的横向方向，其中央导数变化已由原 rank-one 点的惯性分量证明非零，并且其 ordinary-core 变化已精确显示。

原三个固定中央的主目标仍须在其自身来源上完成；附近的 $u$ 依赖来源以及 (31) 的 p 依赖深度不替代该任务。

主要依赖：R728、R759；R761 及公开执行增补 A；原剪切 note 的全权/质量公式。本文不需要新数值执行或生成数据。
