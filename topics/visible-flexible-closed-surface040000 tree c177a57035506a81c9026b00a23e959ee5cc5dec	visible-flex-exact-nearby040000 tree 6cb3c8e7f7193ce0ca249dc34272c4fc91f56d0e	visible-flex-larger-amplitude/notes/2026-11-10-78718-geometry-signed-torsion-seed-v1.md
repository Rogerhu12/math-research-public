# 显式闭嵌入的有符号曲率种子：常标架扭率与零周期积分

作者：Astra-visible-flex-78718bd0 / geometric_closure，2026-11-10。
状态：**完整解析推导加严格整数区间证书，待未参与者全文独审。**
这是一个闭空间曲线及其真实渐近标架；不是二维帽或闭曲面族。
root 独立核验了水平速度和四分弧对称性，并指出必须单独证明四分点
$X\ne0$，这些讨论贡献不充当本稿未参与者独审。

球面副法向积分的经典形式可参见 Larry M. Bates、O. Michael Melko，
*On curves of constant torsion I*，2012，§1，
<https://arxiv.org/abs/1206.7086>。
本稿使用下面另一个明确公式，闭合、嵌入和零周期积分均在本文独证，
不借该文的图像推断某条曲线嵌入。

## 1. 固定的解析球面曲线

对 $t\in\mathbb R$，令

$$
a=\frac{2\sqrt6}{5},\qquad
\rho(t)=\sqrt{1-\frac{24}{25}\cos^2t},\qquad
\vartheta(t)=2t+\frac{13}{6}\sin2t,
$$

$$
B(t)=(\rho\cos\vartheta,\rho\sin\vartheta,a\cos t).
\tag{1}
$$

有 $|B|=1$、$\rho\ge1/5$，所以 $B$ 是周期 $2\pi$ 的解析曲线。
写 $z_B=a\cos t$，直接求导给

$$
|B_t|^2=\frac{(z_B')^2}{1-z_B^2}
 +(1-z_B^2)(\vartheta')^2.
\tag{2}
$$

$z_B'$ 只在 $\pi\mathbb Z$ 为零，而这些点
$\vartheta'=2+13/3=19/3\ne0$。故 $v(t)=|B_t|$ 全圈严格为正。
定义实际空间曲线

$$
\gamma(t)=\int_0^t B(q)\times B_q(q)\,dq.
\tag{3}
$$

它解析且 $|\gamma_t|=|B_t|=v>0$。

## 2. 精确的全部三维闭合

置 $J_z=\operatorname{diag}(1,1,-1)$、
$S_z=-J_z=\operatorname{diag}(-1,-1,1)$。由 (1)，

$$
B(t+\pi)=J_zB(t),\qquad
\gamma_t(t+\pi)=S_z\gamma_t(t).
\tag{4}
$$

因此水平两分量的整周期积分为零。竖分量直接等于

$$
\gamma_{z,t}=\rho^2\vartheta'
=\frac{97}{75}\cos2t-\frac{26}{25}\cos4t.
\tag{5}
$$

其常数项精确为零，所以竖向整周期积分也为零。积分并使用
$\gamma_z(0)=0$，得到

$$
\boxed{\gamma_z(t)=\frac{97}{150}\sin2t
 -\frac{13}{50}\sin4t
 =\sin2t\left(\frac{97}{150}-\frac{13}{25}\cos2t\right).}
\tag{6}
$$

括号至少为 $19/150>0$，因而
$\gamma_z>0$ 于 $(0,\pi/2)$，并按四分区交替符号。
至此 $\gamma(2\pi)=\gamma(0)$，且周期解析速度自动匹配全部 jets。

公式中系数 $13/6$ 的选择有明确来源：一般取
$z_B=a\cos t$、$\vartheta=2t+c\sin2t$ 时，
$\rho^2\vartheta'$ 的平均为 $2-a^2-ca^2/2$。
令其为零给 $c=4/a^2-2$；$a^2=24/25$ 正好给 $c=13/6$。

## 3. 两个严格四分弧门

写 $X=\gamma_x(\pi/2)$、$Y=\gamma_y(\pi/2)$。本节要支付的是

$$
\gamma_{y,t}<0\quad(0<t\le\pi/2),\qquad
X>\frac12,\quad Y<-1.
\tag{7}
$$

速度的精确公式是

$$
\begin{aligned}
\gamma_{x,t}
 &=-a\left(\frac{\sin t}{\rho}\sin\vartheta
       +\cos t\,\rho\,\vartheta'\cos\vartheta\right),\\
\gamma_{y,t}
 &=a\left(\frac{\sin t}{\rho}\cos\vartheta
       -\cos t\,\rho\,\vartheta'\sin\vartheta\right).
\end{aligned}
\tag{8}
$$

令 $\operatorname{sinc}x=\sin x/x$，在 $x=0$ 取解析延拓值 $1$。
则

$$
\begin{aligned}
f(t)={}&\cos\vartheta
-\cos t\,\rho^2\vartheta'
 \left(2+\frac{13}{3}\operatorname{sinc}(2t)\right)
 \frac{\operatorname{sinc}\vartheta}{\operatorname{sinc}t},\\
f(t)={}&\frac{\rho\,\gamma_{y,t}}{a\sin t}quad(0<t\le\pi/2).
\end{aligned}
\tag{9}
$$

第一行在 $t=0$ 也正则；其值为 $-136/225$。
严格区间程序
`../scripts/78718-geometry-signed-torsion-seed.py`
使用**纯整数外向二进区间运算**证明：

- $f<0$ 于整个闭区间 $[0,\pi/2]$；
- 对 (8) 的实际积分，$\int_0^{\pi/2}\gamma_{x,t}\,dt>1/2$，
  $\int_0^{\pi/2}\gamma_{y,t}\,dt<-1$。

以下说明所有计算误差为什么确已包围；它不是浮点网格取样。

### 3.1 π 与外向基本运算

所有区间端点是 $k/2^{128}$。加减用整数精确运算；乘法对四个端点
乘积取最小、最大，再分别向下/向上整除。正区间除法使用
$2^{256}/k$ 的外向整除；平方根使用 Python 整数 `isqrt`，向上端
在不完全平方时加一。每一项均是包含真值的集合运算。

$\pi$ 由 Machin 恒等式
$\pi=16\arctan(1/5)-4\arctan(1/239)$ 包围。
分别取反正切交错级数的 $40$ 项及 $12$ 项，并以第一遗漏项作严格
余量。恒等式可由
$\tan(4\arctan(1/5))=120/119$ 及减角公式验证；对应角位于正确的
第一象限，因此不是仅模 $\pi$ 的等式。

### 3.2 三角函数与显式余项

对所有实际出现的参数，程序先验证其绝对值不超过 $6$。
使用 $24$ 阶偶多项式，也就是从 $k=0$ 到 $24$ 的有限和

$$
P_c(x)=\sum_{k=0}^{24}\frac{(-1)^kx^{2k}}{(2k)!},\qquad
P_s(x)=\sum_{k=0}^{24}\frac{(-1)^kx^{2k}}{(2k+1)!}.
$$

Horner 运算的每一步都外向取整。Taylor 定理及
$\operatorname{sinc}x=\int_0^1\cos(tx)\,dt$ 给全域严格余量

$$
|\cos x-P_c(x)|\le\frac{6^{50}}{50!},\qquad
|\operatorname{sinc}x-P_s(x)|\le\frac{6^{50}}{51!}.
\tag{10}
$$

程序将这些有理数再向上取整成二进端点并加到两侧。
$\sin x$ 由 $x\operatorname{sinc}x$ 作区间乘法。
所有分母在除法前都检验严格正，包括 $\rho$ 与 $\operatorname{sinc}t$。

### 3.3 整个连续区间与积分

写 $t=(\pi/2)x$，$x\in[0,1]$，把 $x$ 分为 $1024$ 个闭区间。
每一盒同时包含不确定但已包围的 $\pi$，并直接区间计算 (9)；
最大上端严格为负。因此盒间没有未检查的空隙。

对 (8) 同样计算每盒函数的上下端，乘以区间 $\pi/2$ 和正有理宽度
$1/1024$，再作外向求和。这是上下 Darboux 和对实际积分的包围，
不使用任何未界定的数值求积误差。求和结果的下端 $X>1/2$、
上端 $Y<-1$ 由纯整数比较确认。

以上完成 (7)。具体区间端点保存于小型回执，不需要进入正文或对话。

## 4. 四分弧的完整集合嵌入证明

再令 $J_y=\operatorname{diag}(1,-1,1)$，
$S_y=-J_y=\operatorname{diag}(-1,1,-1)$，
$S_x=\operatorname{diag}(1,-1,-1)$。
由 (1) 的偶奇性，$B(-t)=J_yB(t)$，故
$\gamma_t(-t)=J_y\gamma_t(t)$，以及

$$
\gamma(-t)=S_y\gamma(t).
\tag{11}
$$

结合 (4)、周期闭合及 $\gamma(0)=0$，得到

$$
\gamma(t+\pi)=\gamma(\pi)+S_z\gamma(t),\qquad
\gamma(\pi-t)=\gamma(\pi)+S_x\gamma(t).
\tag{12}
$$

在第二式取 $t=\pi/2$，使用 (6)，便得
$\gamma(\pi)=(0,2Y,0)$。四个端点因此恰为

$$
(0,0,0),\qquad (X,Y,0),\qquad
(0,2Y,0),\qquad (-X,Y,0).
\tag{13}
$$

由 (7) 它们全部不同。第一四分弧在内部有
$Y<\gamma_y<0$、$\gamma_z>0$，且其 $y$ 坐标严格递减，所以该弧单射。
其余三弧由 (11)–(12) 给出，分别处于下列互不相交的开区域：

| 材料角区间 | $y$ 的开范围 | $z$ 符号 |
| --- | --- | --- |
| $(0,\pi/2)$ | $(Y,0)$ | 正 |
| $(\pi/2,\pi)$ | $(2Y,Y)$ | 负 |
| $(\pi,3\pi/2)$ | $(2Y,Y)$ | 正 |
| $(3\pi/2,2\pi)$ | $(Y,0)$ | 负 |

每弧继承单射性；不同弧的内部不相交，内部也不含 $z=0$ 的端点。
再由 (13) 排除端点重合。这证明 (3) 是实际解析闭嵌入，而非一条
球面曲线闭合之后产生的多重覆盖空间曲线。

## 5. 全圈渐近标架与零周期积分

令 $u(t)=\int_0^t v(q)\,dq$、$\ell=u(2\pi)$，并定义

$$
T=\gamma_u=B\times B_u,
\qquad d=-B_u,
\qquad N=d\times T=-B.
\tag{14}
$$

因为 $|B_u|=1$，这是全圈合法的解析正定向正交标架，包括曲率零点。
由 $d\cdot B=0$，微分得 $d_u\cdot B=1$，所以

$$
\beta=d_u\cdot N=-1,
\qquad \kappa_D=T_u\cdot N=0,
\qquad
\alpha=d_u\cdot T
 =-\frac{\det(B,B_t,B_{tt})}{|B_t|^3}.
\tag{15}
$$

于是实际标架系统是

$$
d_u=\alpha T-N,\qquad
T_u=-\alpha d,\qquad N_u=d.
\tag{16}
$$

$\gamma$ 因而是直纹参考图 $F(r,u)=\gamma(u)+rd(u)$ 的一个真实闭合
渐近曲线；在 $r=0$，$L=C=0$、$M=-1$、$K=-1$。
这里的“常扭率”精确指 (16) 的常标架扭率。在普通曲率非零的每个
连通区间上，通常 Frenet 扭率也等于 $1$；普通曲率零点处不使用没有
定义的商式来冒称 Frenet 标架仍唯一。

由 (4)，$v(t+\pi)=v(t)$，而三重积在反射 $J_z$ 下变号。因此

$$
\alpha(u+\ell/2)=-\alpha(u),\qquad
\boxed{\int_0^\ell\alpha(u)\,du=0.}
\tag{17}
$$

它不是恒零函数。例如在 $t=0$，
$B_t=(0,19/15,0)$、$B_{tt}=(-29/9,0,-a)$，给
$\alpha(0)=-680a/361\ne0$。故 $\alpha$ 确实变号，且只有有限多个
零点；本文不需要预先指定这些零点的重数。

## 6. 首个周期 jet 门已解除，但二维延伸没有支付

对该真实闭合边界保留原直纹共同度量

$$
a_g(r,u)^2=(1+r\alpha(u))^2+r^2,
$$

先前的首 jet 命题化为
$2L_0'=-\alpha L_0^2$。由 (17)，

$$
L_{0,\lambda}(u)
=\frac{\lambda}{1+(\lambda/2)\int_0^u\alpha(s)\,ds}
\tag{18}
$$

在所有充分小的实 $\lambda$ 上都是全圈有限的解析周期解。
所以“没有任何闭嵌入边界能通过首个有符号积分门”不是本题剩余困难。

然而 (18) 只满足接口的一次径向 Gauss–Codazzi 兼容。本文完全没有
断言它延伸成二维共同度量曲面；更高的法向兼容条件仍须检查。
原直纹度量未必合适，也不能把固定几何的这些有限 jets 当作精确帽族。
真正剩余步骤是二维周期 Goursat 单值问题及曲面位置、标架和帽闭合。

## 7. 实际执行身份

冻结源文件：`../scripts/78718-geometry-signed-torsion-seed.py`，6208 B，SHA256
`2eb4e37f881214e2857a22b236a3d4af08f9bf61ea7e3c7a25470e008114b800`。

实际运行命令：

```
python topics/visible-flexible-closed-surface/scripts/78718-geometry-signed-torsion-seed.py --report topics/visible-flexible-closed-surface/notes/2026-11-10-78718-geometry-signed-torsion-seed-check.json
```

2026-11-10 当前执行器工具 `84f447` 自然 exit 0，状态
`PASS_EXACT_OUTWARD_DYADIC_CURVE_SEED_ONLY`。回执1287 B，SHA256
`61eb32fa11aa4ec437c11d2c9318522dac585a154895f89c8d8762aeabfe5942`，
绑定实际运行的源哈希与起止时间。
它没有运行曲面 ODE/PDE，没有生成或检验闭曲面网格。

在写此冻结源之前，作者曾用浮点初探选取 $a^2=24/25$ 并检视四分弧的
单调性。那些浮点结果不是 (7) 的证明；(7) 由这里的独立整数区间执行
重新支付。尚需未参与者复核源码及完整证明并独立重跑。
