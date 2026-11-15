# 2026-11-14：两篇新文献的实际假设与当前非消失缺口

**状态：已核对原文的适用范围；不在此采用尚未在仓库中重证的新算术结论。**
核对日期：2026-11-14。以下只记录会影响当前 O2/O3 与 R540 的具体条件。

## Banwait 的逐素位二次系数判据

Barinder S. Banwait，*Second derivatives of p-adic L-functions and the
Shafarevich–Tate group of rank-two CM elliptic curves*，
arXiv:2609.08431v1，2026-09-08。
[原文](https://arxiv.org/html/2609.08431v1)，§1.1–1.3、Theorem 3.8、§13–15。

Theorem 3.8 的输入包含固定素位处归一二次系数为单位，
并要求曲线满足所列 CM、秩、中心值、符号及坏集条件。
该陈述没有证明这个单位条件在无穷多个素位成立。
§1.2 明确区分已知的逐素位判据与跨素位余秩零问题。
因此这里不把该文的有限计算、形式化或临界值改写当作缺少的无穷非消失。

## Agboola 的 Katz 非临界值公式

A. Agboola，*On Values of the Katz Two-Variable p-adic L-Function*，
2026-04-30 final version。
[作者原稿](https://web.math.ucsb.edu/~agboola/papers/katzval.pdf)，
Assumption 6.1、Theorems 11.1/11.3、Remark 11.4（正文第 27、50–53 页）。

Assumption 6.1 含弱 Leopoldt 与高度配对非退化。
Theorem 11.1 另以相应临界 Katz 值非零为前提；
Theorem 11.3 另列受限 Selmer 秩、局部像和 regulator 条件。
Remark 11.4 中，根数负的相应 p-adic 导数随权非消失仍以期望形式提出，
不是可直接使用的定理。

## 对本课题的实际处理

当前 R540 的原负权带固定有限角色、Schwartz 规范和普通地点。
将它与上述公式比较，仍须逐项识别这些数据并证明所需的秩、局部像和高度条件。
固定 p 改变权的断言也不自动给固定来源随 p 改变的无穷结论。

因此继续原负矩、普通完整补域、惰性同一来源及实际 forcing。
以上核对不关闭任何 open.md 分支，不把研究现状当作停止理由。



## 2026-11-15 增补：同一原 Katz 测度的三个二次方向

以下结论由仓库已证明的
[R40](../results/R40-anticyclotomic-second-coefficient-and-full-selmer.md)
完整 Selmer 主项直接推出；不以 Banwait 新稿代替算术输入。
本节固定 R40 的 $E:y^2=x^3-17x$、$K=\mathbf Q(i)$ 和全部原 ordinary
$p\ge13,\ p\ne17$、有限角色、周期及实际扭转。
只谈这同一曲线，不将式子代给另外三条 $j=0$ 原来源。

记 R40(2)、(29) 的真实双变量测度为
$$
\mathcal K_p(X,Y)\in\mathcal O[[X,Y]],
$$
其中 $(X,Y)$ 是已经移动到 Selmer 中心的同一对 Iwasawa 坐标。
取 $\kappa(\gamma_1)=\kappa^*(\gamma_2)=u=1+p$、
$\kappa(\gamma_2)=\kappa^*(\gamma_1)=1$，固定
$\lambda_p=\log_pu$。

**命题。** 存在 $A_p,B_p\in\mathcal O$ 使
$$
\mathcal K_p(X,Y)
=A_p(X^2+Y^2)+B_pXY\pmod{(X,Y)^3}.
\tag{A1}
$$
这不是预先选择交换对称的生成元；它是当前实际测度的二次项。

证明分两种已付情况。若全 Sha 的余秩 $r_p>0$，
R34 的偶性给 $r_p\ge2$，而 R40(17)、(29) 给
$\mathcal K_p\in(X,Y)^4$，于是二次项为零。
若 $r_p=0$，同两式给二次齐次项为非零共同标量乘
$$
\det(sM+s^*M^t),\qquad M\in M_2(\mathbf Q_p).
$$
该行列式交换 $s,s^*$ 不变，因为交换恰等于转置矩阵。
$X=u^s-1,\ Y=u^{s^*}-1$ 在二阶只贡献相同的 $\lambda_p^2$。
特征生成元到实际 $\mathcal K_p$ 的完整幂级数单位，
因其低于二阶各项为零，也仅贡献一个共同中心值。
因此实际二次项的 $X^2,Y^2$ 系数相等，证明 (A1)。

在这一个测度、这一个生成元和这一个周期下定义
$$
F^\pi_p(T)=\mathcal K_p(T,0),\qquad
F^{\pi^*}_p(T)=\mathcal K_p(0,T),
$$
$$
F^+_p(T)=\mathcal K_p(T,T),\qquad
F^-_p(T)=\mathcal K_p(T,(1+T)^{-1}-1).
\tag{A2}
$$
后一式正是 R40 的原反圆分支。设 $a_2^\square=[T^2]F^\square_p$。
因为 $(1+T)^{-1}-1=-T+T^2+\cdots$，
而 $\mathcal K_p$ 的一次项为零，(A1) 准确给
$$
a_2^\pi=a_2^{\pi^*}=A_p,\qquad
a_2^+=2A_p+B_p,\qquad a_2^-=2A_p-B_p,
$$
$$
\boxed{a_2^++a_2^-=4a_2^\pi.}
\tag{A3}
$$
任何一条分支若另乘其自己的周期或单位幂级数，
都必须先乘回那个**真实中心值**，才能使用 (A3)。
特别不能直接把采用不同归一化的三个数作上述相加，
也不能由非零比较常数推断其为 $p$-adic 单位。

R40 已给 $a_2^-\ne0$ 当且仅当原全 $\Sha[p^\infty]$ 有限。
若 $a_2^-=0$，上述证明实际给三个方向的二次项全为零；
所以另一个方向不能在这个**准确零**的同一素数处救回原判据。
这与有限精度的两个单位判据可能在不同素数失效不矛盾：
$a_2^-\in p\mathcal O$ 和 $a_2^-=0$ 是不同条件。
(A3) 也不证明 $a_2^+$ 在全 Sha 有限时必非零；其自身 regulator 仍须保留。

### 原有限矩的精度和全部中心因子

用 R40(32) 的同一中心测度 $d\mu_\psi=x\,d\mu$，
其中 $x=\psi_{\mathfrak p},y=\psi_{\bar{\mathfrak p}}$，
在全部实际支撑上 $x,y\in\mathbf Z_p^\times$。
置
$$
m=p-1,\quad U=x^m-1,\quad V=y^m-1,
$$
$$
M_{20}=\int U^2\,d\mu_\psi,\qquad
M_{11}=\int UV\,d\mu_\psi,\qquad
M_{02}=\int V^2\,d\mu_\psi.
\tag{A4}
$$
$U,V\in p\mathbf Z_p$，测度有界，所以三个数都属于 $p^2\mathcal O$。
令
$$
M_+=M_{20}+2M_{11}+M_{02},\qquad
M_-=M_{20}-2M_{11}+M_{02}.
$$
此处有准确代数恒等式
$$
M_++M_-=2(M_{20}+M_{02}).
\tag{A5}
$$

另一方面，统一的指数展开给
$$
U=m\log_px+O(p^2),\qquad
V=m\log_py+O(p^2).
$$
故模 $p^3\mathcal O$ 有
$$
M_{20}\equiv2m^2\lambda_p^2 a_2^\pi,\quad
M_{02}\equiv2m^2\lambda_p^2 a_2^{\pi^*},\quad
M_\pm\equiv2m^2\lambda_p^2 a_2^\pm.
\tag{A6}
$$
分母 $2$ 与 $\lambda_p^2$ 来自二阶 Taylor 阶乘及固定 Iwasawa 坐标；
零次和一次矩已由 R40 的完整 Selmer 下界消失。
所以 (A3) 在这一有限精度中成为
$$
M_{20}\equiv M_{02}\pmod{p^3\mathcal O},\qquad
M_++M_-\equiv4M_{20}\pmod{p^3\mathcal O}.
\tag{A7}
$$
因 $v_p(\lambda_p)=1$，(A6) 只决定二次系数模 $p$，
不能将它提升为模 $p^2$ 的结论。

Banwait 原稿 §6.3 的 cyclotomic 三个齐次矩，
在相同 Galois 坐标中读取
$$
Q_+=\int(x^m-y^{-m})^2\,d\mu_\psi.
$$
因为 $y^{-m}=1-V+V^2-\cdots$，准确有
$$
Q_+\equiv M_+\pmod{p^3\mathcal O}.
\tag{A8}
$$
这是可以直接自证的多项式替换范围。
若要把 $Q_+$ 写成其三份 Eisenstein–Kronecker/Hecke 值，
仍须逐项保其 Katz 传送、Euler、阶乘与周期，不能凭 (A8)
省略该比较或把它视为第三个自由二次方向。

还有一个**无需误差展开**的原失败后必要条件。
若全 $\Sha[p^\infty]$ 无限，则已知
$\mathcal K_p\in(X,Y)^4$。
$m=p-1$ 消去有限 Teichmüller 部分；(A4) 中每个矩
都是 $\mathcal K_p(u^{am}-1,u^{bm}-1)$ 的有限整数线性组合，
其中每个坐标属于 $p\mathbf Z_p$，所用 $(a,b)$ 只是
$(0,0),(1,0),(2,0),(0,1),(0,2),(1,1)$。
因此
$$
\boxed{M_{20},M_{11},M_{02}\in p^4\mathcal O.}
\tag{A9}
$$
同理 $Q_+\in p^4\mathcal O$，其实际指数对为 $(2,0),(1,-1),(0,-2)$。
这里没有把模 $p^3$ 的 (A8) 强行提升；每个原 Katz 值本身已有四阶零。
(A9) 是完整 Selmer 的真实共同必要条件，尚未证明在无穷多个 $p$
被指定有限矩违背。

这次增补明确了可以继续使用的两条原二次方向及其共同有限矩；
它不引入新的自由参数，也不证明任何原首系数的跨素数非零。
