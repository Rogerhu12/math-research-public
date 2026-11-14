# R150 附录：任意秩至多三 Hankel 二阶矩的 jet 归约与完整临界分类

日期：2026-11-13（UTC）。作者：Astra-ISP-1cf8c51d。

状态：**已证明。** 本稿付清前稿暂未使用的有限 Hankel/apolar 归约：原 $6\times6$ 复 Hankel 矩阵若秩至多三，就具有唯一总长度等于其秩的曲线 jet 支撑，且各最高 jet 系数非零。因此前稿的完整临界分类适用于全部秩至多三的二阶矩，不再需要另设支撑表示。

证明全部在有限维二元多项式空间中进行，不引用未验证的无限矩延拓或正测度表示。

## 1. 有限二元矩及对称秩列

取任意复 Hankel 矩阵
$$
H=(h_{i+j})_{0\le i,j\le5}.
$$
令 $S=\mathbb C[X_0,X_1]$，$S_k$ 表示齐次 $k$ 次部分。用给定的十一项矩定义线性泛函
$$
\Lambda:S_{10}\longrightarrow\mathbb C,\qquad
\Lambda(X_0^{10-j}X_1^j)=h_j.
\tag{1.1}
$$
对 $0\le k\le10$，置
$$
I_k=\{g\in S_k:\Lambda(gf)=0\text{ 对全部 }f\in S_{10-k}\}.
\tag{1.2}
$$
再令 $I_k=S_k$ 对 $k>10$。这些齐次空间组成理想 $I$：若 $g\in I_k$，则对 $j=0,1$ 及任意 $f\in S_{9-k}$，有 $\Lambda((X_jg)f)=\Lambda(g(X_jf))=0$。

记
$$
b_k=\dim(S_k/I_k).
$$
由 (1.2) 定义的配对
$$
(S_k/I_k)\times(S_{10-k}/I_{10-k})\longrightarrow\mathbb C
$$
在两侧均非退化，因此
$$
\boxed{b_k=b_{10-k}.}
\tag{1.3}
$$
在次数五，配对矩阵准确就是原 $H$，故
$$
b_5=\operatorname{rank}H.
\tag{1.4}
$$
这里没有换用另一个截断矩阵或压缩逆。

## 2. 首个关系的次数准确等于秩

先记录一个二元空间的有限维事实：若 $0\ne U\subset S_k$，则
$$
\boxed{\dim(X_0U+X_1U)\ge\dim U+1.}
\tag{2.1}
$$
证明可取具有不同首项的行阶梯基。设其 $X_1$ 首项指数的集合为 $A$，则 $X_0U+X_1U$ 包含首项指数在 $A\cup(A+1)$ 中的向量。有限非空整数集总有 $|A\cup(A+1)|\ge|A|+1$，故得 (2.1)。

一旦 $I_k\ne0$，理想性质及 (2.1) 给
$$
\dim I_{k+1}\ge\dim I_k+1,
\qquad b_{k+1}\le b_k.
\tag{2.2}
$$
所以首个关系出现后，$b_k$ 不再增长。

若 $H=0$，十一项矩全零，结论为空支撑。以下设
$$
1\le r=\operatorname{rank}H\le3.
$$
此时 $\Lambda\ne0$，故 $I_0=0$。令 $a$ 是 $I_a\ne0$ 的最小次数。由 $b_5=r<6$，有 $1\le a\le5$。
最小性给 $b_{a-1}=a$；对称性给
$$
b_{11-a}=a.
$$
另一方面 $b_a\le a$，而 (2.2) 从 $a$ 起成立。因为 $a\le5<11-a$，得到
$$
a\ge b_a\ge b_5\ge b_{11-a}=a.
$$
于是
$$
\boxed{a=r,\qquad \dim I_r=1.}
\tag{2.3}
$$
取该一维空间的非零齐次生成元 $g\in S_r$。它在射影直线上定义唯一总长度 $r$ 的零点支撑，重根按其重数计入。

## 3. 从唯一关系准确恢复有限 jets

由 $g\in I_r$，$\Lambda$ 杀掉整个 $gS_{10-r}$，因此准确下降到 $r$ 维商
$$
S_{10}/gS_{10-r}.
\tag{3.1}
$$
选一条不经过 $g$ 任一根的射影线性坐标作为无穷远位置；这样的选择存在，因为根只有有限多个。在这个仿射坐标 $t$ 中，$g(t)$ 的次数恰为 $r$，可归一为首一多项式。有限多项式除法给
$$
S_{10}/gS_{10-r}\cong\mathbb C[t]/(g(t)).
\tag{3.2}
$$
若 $g(t)=\prod_\nu(t-z_\nu)^{r_\nu}$，不同因子两两互素。有限 Chinese remainder 分解将 (3.2) 写成
$$
\bigoplus_\nu\mathbb C[t]/((t-z_\nu)^{r_\nu}).
$$
每个加数的对偶基就是在 $z_\nu$ 处的零至 $r_\nu-1$ 阶导数。因此存在且唯一存在系数，使原 $\Lambda$ 对所有次数十的齐次测试多项式准确等于这些有限 jets 的线性组合。

变回原坐标时，局部参数的导数非零，次数十齐次式的局部正规化因子也是单位。有限链式法则和乘积法则只把同一点的 jets 作三角可逆线性变换。因此这个表示准确变回原 $v(z)=(1,z,\ldots,z^5)$ 及无穷远正规列 $(w^5,w^4,\ldots,1)$ 的 jets，既不增加支撑长度，也不产生额外远尾假设。

对每个点，其最高 jet 系数必非零。若有一个为零，就能把该点的支撑长度减少至少一；相应较低次数的根多项式将满足 (1.2)，与 (2.3) 的最小性矛盾。

最后把这个线性泛函作用于所有次数五单项式的乘积，就得到原矩阵的准确表示
$$
\boxed{
H=\sum_\nu\sum_{j=0}^{r_\nu-1}
c_{\nu,j}\left.\frac{d^j}{d\zeta^j}
\big(u_\nu(\zeta)u_\nu(\zeta)^{\mathsf T}\big)
\right|_{\zeta=s_\nu},\qquad
\sum_\nu r_\nu=r,
}
\tag{3.3}
$$
其中各最高 $c_{\nu,r_\nu-1}\ne0$。支撑由唯一的 $g$ 确定，系数由有限商的对偶基确定。

这就付清了前稿所需要的完整 jet 表示；没有假设首个 $r\times r$ 主块可逆，也没有遗漏原坐标的无穷远部分。

## 4. 应用于原六模式立方的全部低秩二阶矩

仍取原完整目标的 $y=V=0$ 截面。前稿[低长度完整临界定理](R150-appendix-gaussian-length-three-critical-support-classification.md)已经对 (3.3) 的每一种长度至多三型证明
$$
v(z)^{\mathsf T}KHKHKv(z)\equiv0
\quad\Longleftrightarrow\quad HKH=0.
$$
现由第1–3节，得到不再预设支撑表示的结论：
$$
\boxed{
\operatorname{rank}H\le3,\quad y=V=0
\quad\Longrightarrow\quad
\big[(y,H,V)\text{ 为完整临界点}\big]
\Longleftrightarrow HKH=0.
}
\tag{4.1}
$$
其全部非零支撑如下。

| 秩 | 准确的完整临界支撑 |
|---|---|
| 一 | 任意曲线点，包括无穷远点；非零复系数任意 |
| 二，两个不同点 | 任意原 $K$ 正交曲线对；有限点满足 $q(s,t)=0$，含无穷远时另一点为 $-1$ |
| 二，一个二重点 | 原有限点 $0,2,-6$ 或无穷远点的一阶 jet；最高 jet 系数非零 |
| 三 | 仅原 $P_+$ 或 $P_-$ 的三个不同根，各点系数非零 |

秩三没有重根或无穷远类型，且其支撑平面恰是原 $W_+$ 或 $W_-$。这使用了已付[长度三曲线 jet 平面分类](R150-appendix-classification-of-isotropic-length-three-curve-jets.md)；秩零是原点。

## 5. 仍然保留的全局缺口

原任意秩至多三的复 Hankel 二阶矩现已完整覆盖，包括首主块退化、重复根及无穷远点。秩四至六不在 (4.1) 的范围内；非零一次矩 $y$ 的一般完整临界点也尚未分类。

在 $y=0$ 截面，全部匹配 $B_r$ 的点值本来就为零。本稿付的是该截面的临界支撑归约，不把点值消失当作新的全局理想归属。局部厚化、一般非零 $y$ 临界分支、真正全局 Bell 自然幂证书及普通 ISP 仍须继续处理。
