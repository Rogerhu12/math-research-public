# 显式闭曲线的直纹端口：精确六秩及正角向第二形式

作者：Astra-visible-flex-78718bd0 / root，2026-11-10。
状态：下述有限维引理给出完整证明及精确有理复算；独立审查待完成。
它给新端口构造的实际初态，尚不提供闭曲面、有效幅度或目标 reach。

## 1. 同一条明确闭嵌入曲线

令 $v\in\mathbb R/(2\pi\mathbb Z)$，并固定

$$
\epsilon=\frac1{10},\qquad
\gamma(v)=(\cos v,\sin v,\epsilon\cos 2v),\qquad
s(v)=|\gamma_v|.
$$

其水平投影是单位圆，故为解析闭嵌入，且 $s\ge1$。
以下 $u$ 是真实弧长，周期为 $\ell=\int_0^{2\pi}s(v)\,dv$，
$T=\gamma_u=\gamma_v/s$。设

$$
D=s^2\gamma_{vv}-(\gamma_v\cdot\gamma_{vv})\gamma_v,
\qquad W=D+\gamma_v\times D,\qquad d=\frac W{|W|}.
$$

若 $c=\cos v$、$b=\sin v$、$z=\epsilon(c^2-b^2)$，则

$$
z_v=-4\epsilon cb,\quad z_{vv}=-4\epsilon(c^2-b^2),\quad
D=(-s^2c+z_vz_{vv}b,-s^2b-z_vz_{vv}c,z_{vv}).
$$

于是 $D\cdot\gamma_v=0$，且
$D\cdot(c,b,0)=-s^2<0$，所以 $D$、$W$ 从不为零。
$d$ 是解析、周期、单位且垂直于 $T$ 的真实法向场。

取 Frenet 标架 $(T,n_F,b_F)$，曲率 $k_F>0$。由上述非零性，

$$
n_F=D/|D|,\quad \gamma_v\times D=s|D|b_F,
\quad d=\frac{n_F+s b_F}{\sqrt{1+s^2}}.
$$

令 $N=d\times T$，则 $(d,T,N)$ 为正定向正交标架。定义

$$
\alpha=d_u\cdot T,\quad \beta=d_u\cdot N,\quad
C_0=T_u\cdot N.
$$

直接分解 $T_u=k_F n_F$ 得

$$
\alpha=-\frac{k_F}{\sqrt{1+s^2}}<0,\qquad
C_0=\frac{k_Fs}{\sqrt{1+s^2}}>0. \tag{1}
$$

若需使用扭率表达式，写 $\theta=\arctan s$，则在上述定向下
$\beta=-(\theta_u+\tau_F)$。这里的符号由
$N=\sin\theta\,n_F-\cos\theta\,b_F$ 决定。

## 2. 标架方程与六维闭合约束的导数

固定函数 $\alpha(u),\beta(u)$，将 $C_0$ 变为可控函数 $C(u)$，解

$$
\begin{aligned}
d_u&=\alpha T+\beta N,&
T_u&=-\alpha d+C N,\\
N_u&=-\beta d-C T,&
\gamma_u&=T.
\end{aligned} \tag{2}
$$

在 $C=C_0$ 时，上节显式闭曲线及标架就是其解，端点的位置与标架均闭合。
将 $G(u)=(R(u),\gamma(u))\in\mathrm{SE}(3)$，$R=(d,T,N)$。
右端写作 $G_u=G\xi$ 时，旋转速度为
$(C,-\beta,\alpha)$，平移速度为第二坐标向量。
因此控制 $\delta C=f(u)$ 对应体坐标无穷小运动 $(f e_1,0)$。
对 ODE 变分并右平凡化，端点导数为

$$
\delta G(\ell)G(\ell)^{-1}
=\int_0^\ell f(u)\operatorname{Ad}_{G(u)}(e_1,0)\,du
=\int_0^\ell f(u)\binom{d(u)}{\gamma(u)\times d(u)}\,du. \tag{3}
$$

改变固定起点或端点局部坐标只会对该六维向量施加一个可逆线性映射，
不影响其满秩性。(3) 同时包含旋转与平移闭合，不能只检查三维旋转。

## 3. 六个有理点的精确行列式

依次选择 $(\cos v,\sin v)$ 为

$$
(1,0),\ (0,1),\ (-1,0),\
\left(\frac35,\frac45\right),\
\left(\frac5{13},\frac{12}{13}\right),\
\left(-\frac35,\frac45\right).
$$

将 (3) 的每个点值列乘以正数 $|W|$，得到
$\mathcal P(v)=(W(v),\gamma(v)\times W(v))^\mathsf T$。
这些列全为有理数，其按上述次序组成的矩阵满足

$$
\det[\mathcal P(v_1)\ \cdots\ \mathcal P(v_6)]
=\frac{15838112388562926448768487424}
 {9876209658570587635040283203125}>0. \tag{4}
$$

所有公式与行列式可由下列无浮点程序逐项复算：
`../scripts/78718-check-ruled-port-rank.py`。
程序直接用有理消元，不调用 ODE、PDE 或曲面优化器。

这给 (3) 的实际满秩性，而非“通常满秩”的一般性断言。
取六点附近互不相交的光滑单位积分 bump，随着支撑宽度趋零，
对应六列积分趋于 (3) 的点值列，故足够窄时其行列式仍非零。

## 4. 控制可以全部位于任意给定开弧

上述点值向量随 $u$ 实解析。若某个非空开弧 $J$ 内的向量张成
真子空间，则存在非零线性泛函 $q$ 在整个 $J$ 上消去它们。
解析恒等定理将 $q\mathcal P=0$ 延拓至整圈，与 (4) 矛盾。
故任意这样的 $J$ 内均可选六个不同点使对应列独立，再用窄的
互不相交单位积分 bump 得到可逆的真实积分矩阵。

将这六个控制 bump 加入 (2)，并添加一个支撑与它们互不相交、仍在
$J$ 内的非零自由 bump。有限维光滑隐函数定理使六个控制系数随
自由系数变化，且在零点附近精确解掉完整六维端点条件。
这一步的详细参数化、固定开弧和像非全等证明由配套构造稿处理；
这里独立支付其所需的初态及导数满秩。

例如对 $J$ 外保留固定开弧，基点置于其补支撑处，则唯一性与最终
完整端点闭合同时固定扰动支撑前后的标架和曲线，不能仅从初始
一段固定就假定末段也固定。

## 5. 与直纹共同度量的关系及边界

对 (2) 的任一真实解，定义 $F(r,u)=\gamma(u)+r d(u)$。
则 $F_r=d$，$F_u=(1+r\alpha)T+r\beta N$，故

$$
g=dr^2+\bigl((1+r\alpha)^2+r^2\beta^2\bigr)du^2
$$

严格不依赖控制函数 $C$。在 $r=0$，第二形式沿 $u$ 的系数为
$C$，基线由 (1) 严格为正；角向度量的一阶径向导数由
$\alpha<0$ 给出。足够小宽度保持真实嵌入性，但本笔记不指定
可见幅度、完整直径、目标 reach 或全曲面闭合。
其拓扑仍是带两个边界的环带；六维端点闭合只闭合材料角变量，
并没有封住径向两边。

## 6. 实际计算身份

初始探索使用终端内联 SymPy 精确有理运算，工具 `2fa44f`，实际
exit 0；它验证了倾斜参数 $\eta=1/10,1/2,1$ 的行列式。
这里仅使用 $\eta=1$，因为未倾斜的纯 Frenet 法向选择使 $C_0=0$。
冻结脚本及其实际重放回执在执行后附下；不把探索后写入的源文件
冒充探索前已经冻结，也不把有限秩检查称为非线性求解或闭面认证。

2026-11-10 当前执行器真实重放：工具 `3fb5bc`，exit 0，
`PASS_EXACT_SIX_COLUMN_RANK_ONLY`。报告
`2026-11-10-78718-root-ruled-port-rank-check.json`，711 B，SHA256
`cea200fb30287df84d815167d50739324ebb0fa8b9a7ac3a1045d488376ece4a`。
报告同时绑定所运行脚本的 SHA256；完整矩阵不进入对话。
