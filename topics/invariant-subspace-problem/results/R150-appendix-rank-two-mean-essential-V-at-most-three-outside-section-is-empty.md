# R150 附录：均值秩二、ess(V) 至多三的外均值截面为空

日期：2026-11-14（UTC）。作者：normal_resume_2220 / Astra-ISP-1cf8c51d。

状态：**已证明。** 保留原六模 Hankel 张量 \(y,H,V\) 与
\[
T_3=y^3-6yH+4V.
\]
若
\[
\operatorname{rank}\operatorname{Cat}(y)=2,\qquad
\operatorname{ess}(T_3)=W,\quad\dim W=3,\qquad
\operatorname{ess}(V)\le3,
\]
并满足原最高方程 \(T_3(Kv(z))\equiv0\)，则必 \(y\in W\)。因此上述条件下的外均值完整临界截面为空；本稿事实上只需最高方程及本质支撑身份，没有使用额外低阶临界假设。

## 1. 一次收缩迫共同支撑准确为四个 jets

记均值的唯一准确长度二物理除子为 \(D\)。若 \(D=s+t\) 约化，写
\[
y=a v(s)+b v(t),\qquad u=a v(s)-b v(t),\qquad ab\ne0.
\]
若 \(D=2s\)，写
\[
y=a v_0+b v_1,\qquad u=v_0,\qquad b\ne0,
\]
其中 \(v_1\) 是真实一阶物理 jet。总有 \(y,u\) 线性独立，且 \(yu\) 是秩二 Hankel 二次张量，准确物理支撑为 \(D\)。

[均值秩二 conormal 归约](R150-appendix-rank-two-mean-five-dimensional-support-and-doubled-maximal-divisor.md)已经证明：
\[
yz\ \text{是 Hankel 二次张量}\quad\Longrightarrow\quad z\in\mathbb Cu.
\tag{1.1}
\]
[最大五 jet 排除](R150-appendix-rank-two-mean-maximal-five-jet-section-is-empty.md)又证明，在本稿的最高方程下，\(y,H,V\) 的准确共同向量支撑 \(E_0\) 维数至多四。

反设 \(y\notin W\)。因为 \(W\) 三维且 \(y\in E_0\)，必 \(\dim E_0=4\)。取
\[
\lambda|_W=0,\qquad\lambda(y)=1.
\]
由 \(T_3\) 的本质支撑，沿 \(\lambda\) 求一次导数得
\[
H-2V\lambda=-2y(H\lambda-y/4).
\]
左侧是 Hankel 张量，故 (1.1) 给某个标量 \(\kappa\)，使
\[
H\lambda=y/4+\kappa u,\qquad
H=2V\lambda-2\kappa yu,
\tag{1.2}
\]
\[
V\lambda^2=\left(\frac18+\frac{\kappa\lambda(u)}2\right)y+\kappa u.
\tag{1.3}
\]
所有乘积、收缩均按原对称张量约定。

若 \(\kappa=0\)，则 \(H=2V\lambda,y=8V\lambda^2\)，使 \(y,H,V\) 全支撑于维数至多三的 \(\operatorname{ess}(V)\)。因 \(W\) 已三维，这会迫 \(y\in W\)，矛盾。因此 \(\kappa\ne0\)。

设 \(D_V\) 是 \(V\) 的唯一最小物理 jet 除子，长度 \(r=\operatorname{ess}(V)\le3\)。该低秩 Hankel 表示及每个顶层局部系数非零，见[共同 jets 归约第六节](R150-appendix-length-three-common-jets-and-inside-mean-critical-dichotomy.md)。

由 (1.2)，共同支撑准确为
\[
E_0=E_{D\vee D_V}.
\tag{1.4}
\]
一侧包含关系直接成立；另一侧使用 \(V\) 的展平像为 \(E_{D_V}\)，且 \(H-2V\lambda=-2\kappa yu\) 的像准确为 \(E_D\)。这里并除子总长度至多五，五次有理正规曲线的全部相应 jets 线性独立。

(1.3) 的右侧非零，因为 \(y,u\) 独立且 \(\kappa\ne0\)。因此 \(E_D\cap E_{D_V}\ne0\)，其准确交除子长度至少一。结合 (1.4)、\(\dim E_0=4\)、\(r\le3\)，只能有
\[
\boxed{r=3,\qquad \deg(D\cap D_V)=1,\qquad
\deg(D\vee D_V)=4.}
\tag{1.5}
\]
这同时排尽了本稿外均值中的 \(\operatorname{ess}(V)\le2\)。

## 2. 共同的剩余长度二块

以下多次出现一个与均值支撑不交的长度二除子 \(R\)，满足 \(\lambda^2|_R=0\)。这里的等式在 \(V_R\) 的真实 Artin 代数中成立：顶层系数非零，使 \(V_R\) 为 Frobenius 泛函，而 (1.3) 在 \(R\) 上的部分为零。

定义
\[
j(z)=z-\lambda(z)y\quad(z\in E_R).
\]
因 \(y\notin E_R\)，\(j\) 单射。由 \(\lambda^2|_R=0\)，准确有
\[
4j^{\otimes3}V_R=4V_R-12yV_R\lambda.
\tag{2.1}
\]
后面将得到
\[
T_3=\gamma w^3+4j^{\otimes3}V_R,\qquad
\gamma\ne0,\quad \operatorname{rank}\operatorname{Cat}(w)\le2,
\tag{2.2}
\]
其中 \(w\) 在均值的长度二空间内且非零，\(w,j(E_R)\) 线性独立。

若 \(R\) 是两个不同点，则 \(\lambda\) 在两点都为零，(2.2) 是三个独立方向上的非零立方和，定义光滑 Fermat 型平面三次。原物理参数化不可能给光滑平面三次的非恒定有理参数化；这也直接属于[本质三维最高支撑分类](R150-appendix-highest-moment-essential-support-and-cubic-projection-types.md)已排除的光滑三次情形。

若 \(R=2q\)，写
\[
V_R=\eta_0v_q^3+3\eta_1v_q^2v'_q,\qquad \eta_1\ne0.
\]
于是 (2.2) 是
\[
\gamma w^3+4v_q^2\big[\eta_0v_q+3\eta_1(v'_q-\lambda(v'_q)y)\big].
\]
三个显示方向独立，重复因子为物理点 \(v_q\)，立方因子 \(w\) 的 Cat 秩至多二，且二者不平行。它被[反向物理重复因子/割线立方因子尖点伴随定理](R150-appendix-no-physical-repeated-factor-secant-cuspidal-companion.md)完整排除。该纯原核定理不要求均值非割线，所以可准确用于这里。

因此只要建立 (2.2)，对应整支就不存在。

## 3. 双点均值 D=2s

由 (1.5)，\(D_V\) 在 \(s\) 的重数准确为一，故
\[
D_V=s+R,\qquad \deg R=2,\quad s\notin R.
\]
写 \(y=a v_0+b v_1,u=v_0\)，\(b\ne0\)。因为 (1.3) 支撑于交除子 \(s\)，其 \(v_1\) 系数必须为零。置 \(A=\lambda(v_0)\)，得到
\[
\frac18+\frac{\kappa A}{2}=0,\qquad
\kappa=-\frac1{4A},\qquad A\ne0.
\]
于是 \(V\lambda^2=\kappa v_0\)，从 \(s\) 处的单点 V 系数可得
\[
\ell=v_0/A,\qquad
V_s=-\tfrac14\ell^3,\qquad
H_D=\tfrac12y\ell-\tfrac12\ell^2.
\]
在其余 \(R\) 上 \(\lambda^2=0\)，且 \(H_R=2V_R\lambda\)。所以
\[
y^3-6yH_D+4V_s=(y-\ell)^3,
\]
\[
T_3=(y-\ell)^3+4j^{\otimes3}V_R.
\]
向量 \(w=y-\ell\) 是非零真实切向长度二方向，Cat 秩为二。其支撑与 \(R\) 不交，三方向独立。第二节遂排除全部双点均值情况，包括原点在无穷远的局部坐标。

## 4. 约化均值，V 在共享点的重数为一

设
\[
D=s+t,\quad s\ne t,\quad
y=a v(s)+b v(t),\quad ab\ne0,
\]
并将唯一交点编号为 \(t\)。因此 \(s\notin D_V\)。

令 \(\alpha=1/8+\kappa\lambda(u)/2\)。在 (1.3) 中，\(v(s)\) 的系数为零，给 \(\alpha+\kappa=0\)，而 \(v(t)\) 的系数为 \(-2b\kappa\ne0\)。在 \(D_V\) 的固定局部 Frobenius 表示中，若 \(t\) 的重数为 \(n\)、\(\lambda\) 的阶为 \(j\)，准确有
\[
n-2j=1.
\]
因为 \(n\le3\)，只可能 \(n=1\) 或 \(n=3\)；重数二已排除。

先取 \(n=1\)。则 \(D_V=t+R\)，其中 \(R\) 长度二且与 \(D\) 不交，且 \(\lambda(v(t))\ne0\)、\(\lambda^2|_R=0\)。置
\[
x=a v(s),\quad z=b v(t),\quad k=\lambda(z)\ne0.
\]
于是 \(\lambda(x)=1-k\)，而 (1.3) 给
\[
\kappa=-\frac1{4(3-2k)},\qquad 3-2k\ne0.
\]
均值块的完整张量为
\[
H_D=\frac{kx^2+(2-k)z^2}{2k(3-2k)},\qquad
V_t=\frac{z^3}{2k^2(3-2k)}.
\]
直接展开原普通第三矩得
\[
y^3-6yH_D+4V_t
=-\frac{2}{k^2(3-2k)}
 \big[kx-(1-k)z\big]^3.
\tag{4.1}
\]
附属整数验证器在乘去 \(k^2(3-2k)\) 后逐项核验此式。

令 \(w=kx-(1-k)z\)。它非零、Cat 秩至多二，允许 \(k=1\) 时退为物理单点；其与 \(R\) 的支撑仍不交。其余部分由 (2.1) 给出，因此得到 (2.2)，由第二节排除。

## 5. 约化均值，V 全支撑在共享三重 jet

最后 \(n=3\)，故 \(D_V=3t\)，且 \(\lambda\) 在 \(t\) 的准确局部阶为一。以原物理代表上 \(\lambda(v)\) 的值作为局部参数，取 Taylor jets \(v_0,v_1,v_2\)，使
\[
\lambda(v_0)=0,\quad\lambda(v_1)=1,\quad\lambda(v_2)=0.
\]
这是合法局部坐标，包括无穷点；\(v_1\) 仍是真实一阶 jet，允许非零比例和加一个 \(v_0\) 倍数。

令 \(x=a v(s)\)，则 \(y=x+bv_0\)、\(\lambda(x)=1\)、\(\lambda(u)=1\)。式 (1.3) 给
\[
\kappa=-1/12,\qquad
V=\eta_0v_0^3+3\eta_1v_0^2v_1
 +\frac b2(v_0^2v_2+v_0v_1^2).
\]
式 (1.2) 随即给
\[
6H=x^2+(12\eta_1-b^2)v_0^2+4b\,v_0v_1.
\]
将这两个原张量直接代入 \(T_3=y^3-6yH+4V\)，得到
\[
T_3=v_0\Big[
2b(v_1-x)^2+
v_0\big(2bv_2+(12\eta_1-4b^2)(v_1-x)
 +(2b^3-12b\eta_1+4\eta_0)v_0\big)
\Big].
\tag{5.1}
\]
附属脚本在整数多项式环中核验 (5.1)。

原 \(v_0\) 的极线非零，且 \(b\ne0\)。因此最高方程迫
\[
K(v_0,v(z))\ \big|\ 
\big[K(v_1,v(z))-K(x,v(z))\big]^2.
\]
但 \(x=a v(s)\)，\(s\ne t\)，而 \(v_1\) 是 \(t\) 处的真实一阶 jet。这正违反[原异点平移切向 conic 伴随禁阻](R150-appendix-no-physical-shifted-tangent-conic-companion.md)。该定理明确允许局部 jet 的非零缩放及加 \(v_0\) 倍数，且已覆盖全部有限、无穷及特殊物理点。

## 6. 结论与继续范围

(1.5) 列出的交长度一情形已全部处理。外均值假设产生矛盾，所以本稿最高方程截面必有 \(y\in W\)。特别，原完整临界点在 Cat 均值秩二、本质第三矩维数三、\(\operatorname{ess}(V)\le3\) 下不能有外均值。

仍需继续的是本稿同一低 V 类中的内均值及其可能的共同四维支撑；满 \(\operatorname{ess}(V)=4\) 类由并行主线处理。本稿不支付全局匹配 Bell 自然幂、原实际逆或普通 Hilbert ISP 的最终结论。
