# R72. 对称幂除素数缺陷与实际挠点投影

日期：2026-11-12。**状态：完整混合商、实际投影和临界有限和已证明；总和的跨素数非零未证明。**

## 1. 模平方保留的真实混合商

对特征 $p>2$ 的秩二空间 $V=kX\oplus kY$，有等变正合列
$$
0\longrightarrow V^{(1)}\longrightarrow\operatorname{Sym}^pV
\longrightarrow\operatorname{Sym}^{p-2}V\otimes\det V\longrightarrow0.
$$
商映射将 $X^{p-j}Y^j$ 送至
$jX^{p-j-1}Y^{j-1}\otimes(X\wedge Y)$，两个端点送零。
此式按基变换黏合，也与 GM 连接相容。

模 $p^2$ 的混合 lift 缺陷为
$$
\mathcal C_c=\frac{(X+cY)^p-X^p-c^pY^p}{p}.
$$
当 $c$ 遍历 $\mathbb F_p^\times$，其商像张成整个秩 $p-1$ 商；
由有限域角色正交可以逐个恢复所有单项式基。
甚至不存在模 $p^2$ 的秩二自由直和因子，既提升
$kX^p+kY^p$ 又对 $Y\partial_X$ 稳定：提升 $X^p$ 的微分中
$pX^{p-1}Y$ 项不能由任何 $p$ 倍修正消掉。
这排除一般自然两维提升，不排除特殊系统的其他相对实现。

## 2. 原 256 项投影后的准确有限和

取惰性 $p\ge7$，沿用 R68：
$$
B=U/(V/t)=1-t^2+\cdots,\qquad
W=M_1U/((1-4t^2)(V/t)^2)=t^4+\cdots.
$$
令 $b=B-1$、$r=(p-3)/2$。二项式展开给特征零准确等式
$$
\frac{C_{p+1}}p=\frac{W_{p+1}}p+
\sum_{j=1}^{r}\frac{\binom pj}{p}[t^{p+1}]Wb^j.
\tag{1}
$$
这里 $W_{p+1}/p$ 整，是由实际 $C_{p+1}\in p\mathbb Z_p$ 推出。
式 (1) 模 $p$ 的二项系数为 $(-1)^{j-1}/j$。

原 68 级标签的两个 256 项和只作用在 $M_1$，与公共 $U,V,B$ 交换。
所以实际投影后的混合级数就是 $Wb^j$，其首项
$(-1)^jt^{4+2j}$ 给目标 jet 内 $(p-3)/2$ 维的三角独立空间。
不能再以挠点角色正交逐项消去它们；这个三角秩也不是任意几何实现的最小秩断言。

最后一个 $j=r$ 项的实际临界贡献恒为
$$
\frac{(-1)^{r-1}}r[t^{p+1}]Wb^r=-1/r=2/3\pmod p.
$$
因此目标首层非零准确还需控制其余实际和不等于 $-2/3$。
恒非零末项本身不排除抵消。

规范
$C_{p+1}=(p+1)!\beta_{p+1}^2/(24\,17^{p-3})$
使 (1) 模 $p$ 非零等价于 $\beta_{p+1}$ 为单位，因而足以初级有限。
完整证明见 [GM 对称幂与实际投影](../notes/2026-11-12-gm-symmetric-power-bockstein-and-torsion-projection.md)。
