# R978 — 原13-old 两退化、全部相位与 F10 余项的完整中央非零

日期：2026-11-26 UTC。**已证明：原 degree130 的两处13-old二维块由真实 degree10 算术线的两个原13拉回完整张成；原 R971 六 sigma 候选的 $E_{125}$ 旧部分恰为非零质量零差。它在 R968 同一普通射线的完整单位 Mellin 导数非零，并在每个充分大的好惰性素数处有精确非零的完整 Newton 导数。** 这是实际旧来源的中央值，不是新 rank≥2 曲线的 Sha 结论，不能传播给 $F_{11}$ 的其他块或 whole companion。

沿用 $K=\mathbf Q(\omega)$、$\delta=1+2\omega$、$\delta^2=-3$，
$$
 \pi=\pi_{13}=4+\omega=(7+\delta)/2,\qquad N\pi=13.
 \tag{1}
$$
本篇的 $F_{10}$ 指 R971 中最后一个整数系数为10的、degree130的六 sigma 来源；不是 degree10 的函数。

## 1. 两个真实拉回的完整除法载体

共同 $E_1:y^2=x^3+1$ 的 degree10 主型空间是
$$
 V_{10}=\sigma^{10}x^2K[X]_{\le1}
       =K e_0\oplus K e_1,\qquad
 e_0=\sigma^{10}x^2,\quad e_1=\sigma^{10}x^5,\quad X=x^3.
 \tag{2}
$$
其中 $e_0(0)=0,e_1(0)=1$。定义 raw pull
$$
 D_\pi f(z)=f(\pi z),\qquad D_{\bar\pi}f(z)=f(\bar\pi z).
 \tag{3}
$$
它们没有附加 Hecke 值或 $\pi^{-1}$ 归一；后者属于不同的 pull–trace 算子。

原 norm13 division 比准确为
$$
 \sigma(\pi z)=\pi\,\sigma(z)^{13}R(X),\qquad
 2\pi R(X)=7X^2-4X+16+\delta(X^2+44X+16).
 \tag{4}
$$
$R$ 是首一二次多项式，等价于
$R=X^2+(2+6\delta)X+(40+24\delta)/13$。
保原微分 $dz=dx/(2y)$，直接对 (4) 取二次对数导数，得
$$
 x(\pi z)=\frac{x A(X)}{\pi^2R(X)^2},
 \tag{5}
$$
$$
 \boxed{A=13R^2-6(7X+4)RR'
       -36X(X+1)(RR''-R'^2).}
 \tag{6}
$$
这里使用
$(dX/dz)^2=36xX(X+1)$、$d^2X/dz^2=6x(7X+4)$。
$A$ 的四次首项系数为 $13-84+72=1$；其三次系数为
$24-28(2+6\delta)=-32-168\delta$。

将 (4)–(5) 代入 (2)，两列在完整22维标准基中的多项式是
$$
 \boxed{
 \frac{D_\pi e_0}{\sigma^{130}x^2}
       =\pi^6 A^2R^6,\qquad
 \frac{D_\pi e_1}{\sigma^{130}x^2}
       =X A^5.}
 \tag{7}
$$
另一对列逐项共轭。两式的次数分别为20、21，顶端系数为 $\pi^6,1$；所有分母已在整条式中消去。尤其
$$
 (D_\pi f)(0)=(D_{\bar\pi}f)(0)=f(0).
 \tag{8}
$$
这固定了旧向量的质量相位，不能把它们另乘 $\psi(\pi)^{-1}$ 后仍使用 (8)。

若需要算术归一的旧向量，R973(8)–(10) 给 $E_{125}$ 的
$\psi_{125}((\pi))=\omega^2\pi$、$\psi_{125}((\bar\pi))=\omega\bar\pi$；
$E_{12500}$ 的两值则是 $\pi,\bar\pi$。例如第一条由全局 $\pi$
在2、3、5的单位值 $\omega,-1,-1$ 得到。这样的归一只改变 (7) 的明确标量，不能代替本篇固定的 raw pull。

## 2. 有限13重数二确实就是这两个旧方向

R973 已由实际矩阵证明，split $T_{13}$ 的有限 Weil 表示有全部十二个角色，只有 quadratic $\tau_6$ 的重数为二。它的算术单位角色为平凡，即13未分歧的同一个全局 Hecke 角色。

在 split Schrödinger 极化中，
$$
 W_{13}(\operatorname{diag}(t,t^{-1}))f(a)
      =\left(\frac t{13}\right)f(ta).
 \tag{9}
$$
quadratic 等型部分准确由 $\delta_0$ 与常数向量 $\mathbf1$ 张成：在
$\mathbf F_{13}^{\times}$ 上不变的函数由零点值和非零轨道值唯一确定。
这也直接给其维数二，而不是从“出现两次”任选两个向量。

两个互补 isotropic 核 $\ker[\pi]$、$\ker[\bar\pi]$ 在13-torsion中横截；各自的 canonical Heisenberg 固定线分别是 $\delta_0$ 与 $\mathbf1$。原拉回 $D_\pi,D_{\bar\pi}$ 的像分别具有这两个核的平移不变性，故它们在有限13因子中就是上述两线。R970 的 isometry 仅把这两线送到其固定极化下的完整13坐标，并不改变它们的独立性。

在无限局部 Schrödinger 模型中，这两向量对应两个格指标
$\mathbf1_{\mathbf Z_{13}}$、$\mathbf1_{13\mathbf Z_{13}}$
（连同已固定 isometry 与非零规范）。非紧 uniformizer 把格移到相邻格；
不能声称两个有限向量各自固定于非紧环面。其参数已经由 R973 的主
idèle 公式付清。本篇使用真实退化映射 (3)–(7)，因而不用从好位谱决定一个非紧向量。

将2、5两个有限因子同时保留，上述结论给
$$
 D_\pi V_{10}+D_{\bar\pi}V_{10}
 =V_{130}^{(b=6)},\qquad \dim_K V_{130}^{(b=6)}=4.
 \tag{10}
$$
两个好位的原 pull–trace 与 (3) 交换；这是互素核的完整纤维基变换，所有 division 比和除数 $\gamma$ 同时保留。因此 (10) 在 R973 的两个算术类型上分别成为
$$
 \begin{aligned}
 V_{130}^{(1,0)}&=K D_\pi\Psi_{125}
                       \oplus K D_{\bar\pi}\Psi_{125},\\
 V_{130}^{(5,4)}&=K D_\pi\Psi_{12500}
                       \oplus K D_{\bar\pi}\Psi_{12500}.
 \end{aligned}
 \tag{11}
$$
右边每条 $\Psi_d$ 是 $V_{10}$ 中真实 primitive 算术线的一个非零向量；
好位特征值与 R973 相同，绝非两条新曲线。也可从 (7) 的完整四列及两好位算子严格下推得到同一分解。

两个 raw pull 在每条非零线上都独立。一个直接解析核查是：若
$\Psi(\pi z)=c\,\Psi(\bar\pi z)$，对任意两个非零 Taylor 项的次数
$r\ne s$ 比较，得 $(\pi/\bar\pi)^{r-s}=1$。这不可能，因为
$\pi/\bar\pi$ 在两个13素理想处的赋值为 $1,-1$。非零正 degree theta 截面不能只有一个 Taylor 单项式，否则它不满足其真实准周期。故 (11) 是直和。

R976 已在完整22列上读得这两个二维块的质量泛函均非零。由 (8) 与
(11)，各自 primitive $\Psi_d(0)\ne0$。因此可以唯一归一
$$
 \Psi_{d,1}=\sigma^{10}x^2(X+c_d),\qquad \Psi_{d,1}(0)=1.
 \tag{12}
$$
此处质量非零来自真实全矩阵和全部旧退化，不使用“代数秩零推出解析秩零”这一未付推论。

每个二维块的质量零子空间因而准确是
$$
 \boxed{K\Delta_d,\qquad
 \Delta_d=D_\pi\Psi_{d,1}-D_{\bar\pi}\Psi_{d,1}.}
 \tag{13}
$$
没有隐藏根单位相位。两个好位不能进一步分开同一 (11)，但质量与真实 raw pull 已固定 (13)。

## 3. 原 F10 余项是实际非零差

R971 的整个 degree130 来源记为 $F_{10}$，归一为首阶六、首项一。
R976 的全81块计算已证明它只在两个块上非零：
$$
 \Pi_{(4,3)}F_{10}=-\frac{11}{2}\Phi_{65^3,1},
 \qquad
 R_{10}:=\Pi_{(1,0)}F_{10}
       =F_{10}+\frac{11}{2}\Phi_{65^3,1}\ne0.
 \tag{14}
$$
两条来源的质量均零，首阶均六、首项均一，所以
$$
 R_{10}(0)=0,\qquad[z^6]R_{10}=13/2.
 \tag{15}
$$
结合 (13)，存在唯一固定 $\kappa_{10}\in K^\times$ 使
$$
 \boxed{R_{10}=\kappa_{10}
       \bigl(D_\pi\Psi_{125,1}-D_{\bar\pi}\Psi_{125,1}\bigr).}
 \tag{16}
$$
这是真实完整函数身份；它由全块支撑、完整维数与质量泛函推出，不是仅用 (15) 两个 jet 拟合。

也可以给该标量的准确表达。原 sigma 和 $x$ 展开给
$$
 \Psi_{125,1}(z)=1+(c_{125}-2/3)z^6+O(z^{12}),\qquad
 \pi^6-\bar\pi^6=2520\delta.
 \tag{17}
$$
故 (15) 迫 $c_{125}\ne2/3$，并且
$$
 \kappa_{10}=\frac{13}{5040\delta(c_{125}-2/3)}\ne0.
 \tag{18}
$$
$c_{125}$ 是 (12) 的唯一已指定 primitive 源系数；完整读数器从同次矩阵下推后直接返回它和 (18)，不把它作为外部生成系数输入。

R977 的新 $F_{11}$ 不享有 (16) 的前提。其实际两处13-old质量分别为
$1/297,-5/2376$；所以至少这两项都必须保一般的
$aD_\pi\Psi+bD_{\bar\pi}\Psi$，不能改成质量零差。它的非六次块也全部保留。

## 4. 普通完整单位 Mellin 身份

本节固定 R968 的同一普通素数射线、同一共同曲线与微分、同一 whole
$\mathcal S_{10}$ 测度格。其实际全核已经支付
$$
 \nu_\Psi|_{p\mathbf Z_p}
       =\upsilon_p[\kappa_p]_*\nu_\Psi,\qquad
 \upsilon_p=\chi_{10}\lambda_p,\quad \chi_{10}\in\{\pm1\},
 \tag{19}
$$
这里 $\lambda_p,\kappa_p$ 是 R968 的原量，不能将本篇的固定
$\kappa_{10}$ 与 $\kappa_p$ 混同。
全 $\mathcal S_{10}$ 的绝对标量来自该篇的实际双变量 odd degree5 拉回；
它不是单变量乘积的核相乘。R410 已付 $1\pm\lambda_p$ 为单位。

对质量一 $\Psi$，在 (19) 取全质量，得到准确的原单位质量
$$
 \boxed{\nu_\Psi(\mathbf Z_p^\times)=1-\upsilon_p\in\mathcal O^\times.}
 \tag{20}
$$
这是同一真实单位切域，不将全质量1当成单位质量1。

定义原 principal Mellin
$$
 J_{\Psi,p}(u)=\int_{\mathbf Z_p^\times}\langle x\rangle^u\,d\nu_\Psi(x).
 \tag{21}
$$
本篇此处的 $u$ 准确指指数 $u$。接入 R968 使用指数 $(p-1)v$ 的
原权变量时，始终写
$J^{[p-1]}_{\Psi,p}(v)=J_{\Psi,p}((p-1)v)$；
其零点导数是本篇 $u$ 导数的 $(p-1)$ 倍，不将两种变量混用。
在当前普通嵌入中 $\pi,\bar\pi\in\mathbf Z_p^\times$。原 Amice
$D_\pi\Psi$ 的测度准确为 $[\pi]_*\nu_\Psi$，因为
$\Psi(\pi\Omega_p\log(1+Z))$ 正是推前的完整生成函数。
乘 $\pi$ 保持整个单位域，故对每个 $u\in\mathbf Z_p$
$$
 \boxed{J_{D_\pi\Psi,p}(u)=\langle\pi\rangle^uJ_{\Psi,p}(u),\qquad
 J_{D_{\bar\pi}\Psi,p}(u)=\langle\bar\pi\rangle^uJ_{\Psi,p}(u).}
 \tag{22}
$$
这不是逐权模 $p$ 同余，也没有删除 tame/深域：principal 中
Teich 部分为一，若取非 principal 第 $k$ 支，则右边另保
$\omega_p(\pi)^k$ 或 $\omega_p(\bar\pi)^k$。

(13)、(20)–(22) 给完整中央
$$
 J_{\Delta_d,p}(0)=0,\qquad
 \boxed{J'_{\Delta_d,p}(0)
   =\log_p\langle\pi/\bar\pi\rangle\,(1-\upsilon_p).}
 \tag{23}
$$
若采用 Amice 权变量 $T$ 而非 $u$，$G(T)=J(\log(1+T)/\log(1+p))$，
则右边还须除以 $\log_p(1+p)$，不混用两种导数。

对每个好普通 $p$，$\log_p(\pi/\bar\pi)\ne0$：它是一个 $p$-adic
单位，若对数为零，则其 $(p-1)$ 次幂为一。嵌入 $K\hookrightarrow
\mathbf Q_p$ 单射，遂使 $\pi/\bar\pi$ 成为全局根单位，与两个13赋值
$1,-1$ 矛盾。因此 (23) 对 R968 同一无限普通射线逐 $p$ 非零；
当使用 $R_{10}$ 时只另排固定非零 $\kappa_{10}$ 的有限坏集。

### 4.1 共同物理模型的精确缩放

degree10 的质量一来源齐次式为
$$
 \Psi_{d,b}(z)=\sigma_b^{10}x_b^2(x_b^3+c_db)
            =\Psi_{d,1}(\theta_bz),\qquad\theta_b^6=b.
 \tag{24}
$$
它没有 overall $b^{-1}$。六 sigma 的 $F_{10}$ 与 degree130 算术
$\Phi_{65^3}$ 则有 overall $b^{-1}$；故 (16) 在共同 $b=17$ 上是
$$
 R_{10,17}=\frac{\kappa_{10}}{17}
     (D_\pi\Psi_{125,17}-D_{\bar\pi}\Psi_{125,17}).
 \tag{25}
$$
所以真正同一原微分及格的 ordinary 导数为
$$
 \boxed{J'_{R_{10,17},p}(0)
   =\frac{\kappa_{10}}{17}
      \log_p\langle\pi/\bar\pi\rangle\,(1-\upsilon_p)\ne0.}
 \tag{26}
$$
在 R968 的指数 $(p-1)v$ 变量中，准确变为
$$
 (J^{[p-1]}_{R_{10,17},p})'(0)
 =\frac{\kappa_{10}}{17}(p-1)
       \log_p\langle\pi/\bar\pi\rangle(1-\upsilon_p)\ne0.
 \tag{26a}
$$
固定17虽为当前单位，仍不在准确身份中删除。

更一般地，对当前任何一个实际块
$A_b=b^{-1}(aD_\pi\Psi_{d,b}+b_0D_{\bar\pi}\Psi_{d,b})$，完整式为
$$
 \begin{aligned}
 J_{A_b,p}(0)&=b^{-1}(a+b_0)(1-\upsilon_p),\\
 J'_{A_b,p}(0)&=b^{-1}\bigl((a+b_0)J'_{\Psi_{d,b},p}(0)\\
 &\qquad+(a\log_p\langle\pi\rangle+
              b_0\log_p\langle\bar\pi\rangle)(1-\upsilon_p)\bigr).
 \end{aligned}
 \tag{27}
$$
当 $a+b_0\ne0$，原 primitive 导数项确实存在；不能借 (23) 抹去它。

## 5. 同一个来源的完整惰性 Newton 差

这一结论不要求 R968 的普通射线。令 $p>211$ 好惰性、
$d=p+1$，在共同 $E_1$ 上保持 R301 的
$c_p=[z^d]\log(\sigma/z)$、$v_p(c_p)=-1$。对任意实际质量一
$\Psi_{d_0,1}\in V_{10}$，使用它自己的 charge10 Gaussian：
$$
 B_{10}(z)=\Psi_{d_0,1}(z)e^{-10c_pz^d},\qquad
 b_h=(10c_p)^{-h}[z^{dh}]B_{10},\qquad
 J_{10,p}(v)=\sum_{h\ge0}b_h(v)_h.
 \tag{28}
$$
这里 $d_0=125$ 或12500是曲线参数，与 $d=p+1$ 区分。
完整圆盘估计在质量列也成立：
$$
 v_p(b_h)\ge\left\lceil\frac{h(p-1)}{2p}\right\rceil
 \quad(h\ge1),\qquad b_0=1.
 \tag{29}
$$
于是 $J_{10,p}\in1+p\,v\mathcal O\langle v\rangle$，特别
$J_{10,p}(0)=1$。取源系数的固定有限坏集之外即可，不要求某个有限
首位先非零。

把 $D_\pi\Psi$ 放入 level130 时，须使用 charge130 的同一个参考
Gaussian $130c_p$。完整有限 Gaussian 卷积恒等式在每整数 $k\ge0$ 给
$$
 \begin{aligned}
 J_{130,D_\pi\Psi,p}(k)
  &=k!(130c_p)^{-k}[z^{dk}]\Psi(\pi z)\\
  &=\left(\frac{\pi^d}{13}\right)^k
         k!(10c_p)^{-k}[z^{dk}]\Psi(z)
   =q_\pi^kJ_{10,p}(k),\\
 q_\pi&=\pi^d/13.
 \end{aligned}
 \tag{30}
$$
同样 $q_{\bar\pi}=\bar\pi^d/13$。惰性 Frobenius 在
$\mathbf F_{p^2}$ 上为共轭，所以
$$
 q_\pi,q_{\bar\pi}\in1+p\mathcal O.
 \tag{31}
$$
$q_\pi^v$ 因而是同一 Tate 盘上的整解析函数。两边均为受限解析函数，
整数在 $\mathbf Z_p$ 稠密，(30) 唯一延拓为完整函数身份
$$
 \boxed{J_{130,\Delta_{d_0},p}(v)
       =(q_\pi^v-q_{\bar\pi}^v)J_{10,p}(v).}
 \tag{32}
$$
没有截去 Gaussian 余项，也没有假定它等于零；$13$ 的归一正是两种
真实 charge 的比。

在零点求导，得到
$$
 \boxed{J'_{130,\Delta_{d_0},p}(0)
       =\log_p(q_\pi/q_{\bar\pi})
       =(p+1)\log_p(\pi/\bar\pi)\ne0.}
 \tag{33}
$$
惰性局部域中对数的单位核是有限根单位；若右边为零，单射
$K\hookrightarrow K_p$ 同样使 $\pi/\bar\pi$ 成为全局根单位，
与两个13赋值矛盾。

将 (24)–(25) 的整微分同构及 Gaussian 同时运输到物理 $b=17$，
所有 $\theta_b^{dh}$ 在 Newton 系数中相消，唯有 (25) 的固定
overall 标量保留。因此原共同模型的精确结论是
$$
 \boxed{J'_{130,R_{10,17},p}(0)
       =\frac{\kappa_{10}}{17}(p+1)
          \log_p(\pi/\bar\pi)\ne0.}
 \tag{34}
$$
它对所有充分大的好惰性 $p$ 成立，不是有限素数扫描或首位同余。

## 6. 整个来源的可消费结论与限制

由完整来源恒等式 (14)，ordinary 的同一真实单位测度导数满足
$$
 J'_{F_{10,17},p}(0)+\frac{11}{2}J'_{\Phi_{65^3,17},p}(0)
   =J'_{R_{10,17},p}(0)\ne0
 \tag{35}
$$
于 R968 射线；inert 的 charge130 Newton 也有完全相同的线性身份，
其右边由 (34) 给出。这里三项 degree、Gaussian 与物理规范完全一致。
因此不能在当前原格中同时把 $F_{10}$ 和 $\Phi_{65^3}$ 的完整导数
设为零。

但 $F_{10}$ 是六 sigma 边际，不是另一条已证明 rank≥2 曲线的
primitive 来源；$R_{10}$ 也只是 $E_{125}$ 的两个旧向量之差。
式 (35) 本身没有完成课题。要在原多变量观察中使用它，必须继续保
完整 companion、真实单位/深切域和观察次序，不能把一维边际恒等式
传播到任意 mixed cut。尤其 $F_{11}$ 的一般旧分量适用 (27)，其余
primitive 和非六次块仍逐项存在。

## 7. 同次 v7 完整实际回执：两条 primitive 整源和所有旧系数

公开 [run 45888699507](https://github.com/Rogerhu12/math-research-public/actions/runs/45888699507)、job **140145723941**、源提交
aa6939d6012a5d00066022af37477670b045e85d 已全部 PASS。
old 消费者为14144字节，SHA256
7084ff005adb174051a5fb84e1a3e296babca78452d51ed9f95b7752f44a7c49；
入口 SHA256 为
53478585af0add137ca81aa591cdd48bd21546a040aac064923ef1ccc58ddca7。
它从同次原完整390矩阵重新限制全部22列，现造 (7) 的四列，
两个方向都全22回乘，并严格下推相同的 $V_{10}$ 两个 CM 算子。
四列秩准确为4，两条 primitive 角色各秩一，两pull各完整张成相应二维旧块。

实际 `2026-11-26 20:07:29` 至 `20:13:49 UTC`，结论 `success`；
入口 `372.726615119` 秒，old 消费者 `0.193138416` 秒；`python-flint 0.9.0`，4 workers。
全部18源 manifest SHA256 `c199dda0322a404ed70097b84f0ec497ec0d60f619414d457fb97b3dafdc8de3`；
stdout 71448 B，SHA256 `3327ca3286386a389da1dd73c02806d60e6fe4be20d0b78d692b9895be3857b5`；
完整 job log 168278 B，SHA256 `bacd9b9a4fb33870d9775a4bbc1e518e58fa0fa736ed7e99ce4f327362d94c36`。
所有生成系数、矩阵和日志均不入仓库或 Release；原同次所有 v6 数学门保留。

实际返回的质量一原源是
$$
 \boxed{\Psi_{125,1}=\sigma^{10}x^2(X-8),\qquad
        \Psi_{12500,1}=\sigma^{10}x^2(X+10).}
 \tag{36}
$$
它们全有理、全整，质量均为一。其源摘要分别是
95c903b5d2f46a030371817bb9b036c4e593fe0d1433b828d50049eaa5395dc2、
0ff784f0522c98d4db6fd32371307ca04e6fd5efc3f95b70028af0b0bf8e7cd5；
完整 $V_{10}$ 两矩阵摘要为
4d58f7926499a810b9696277093f331925f6531ec968666798ab9deeb3e25c70。
两条未归一差首项分别为 $-21840\delta,23520\delta$，均准确六阶。
所有坐标来自该次全算子回乘，不以源摘要或两个首项代替证明。

下表每行准确表示 $aD_\pi\Psi_d+b_0D_{\bar\pi}\Psi_d$，
所有等式都在全部22行返回：

| 原源、算术块 | $a$ | $b_0$ | 质量 |
|---|---|---|---|
| $F_{10}$，$E_{125}$ | $\delta/10080$ | $-\delta/10080$ | $0$ |
| $F_{11}$，$E_{125}$ | $(4+\delta)/2376$ | $(4-\delta)/2376$ | $1/297$ |
| $\mathscr H_{130}$，$E_{125}$ | $(1+\delta)/2041200$ | $(1-\delta)/2041200$ | $1/1020600$ |
| $F_{10}$，$E_{12500}$ | $0$ | $0$ | $0$ |
| $F_{11}$，$E_{12500}$ | $(-5-\delta)/4752$ | $(-5+\delta)/4752$ | $-5/2376$ |
| $\mathscr H_{130}$，$E_{12500}$ | $(-1+\delta)/2041200$ | $(-1-\delta)/2041200$ | $-1/1020600$ |

因此 (18) 的原标量已具体为
$$
 \boxed{\kappa_{10}=\delta/10080,}
 \tag{37}
$$
与 $c_{125}=-8$ 独立代回 (18) 完全一致。当前 $p>211$ 时，
这个标量和本文所示清分母均为单位；(26)、(26a)、(34) 不再有未计算的
来源坏素数需要另排。

### 7.1 原 H/F11 两个不同旧块中的准确质量抵消

记 $H_d=\Pi_d\mathscr H_{130}$、
$F_{11,d}=\Pi_dF_{11}$、$F_{10,d}=\Pi_dF_{10}$，
其中 $\Pi_{125}=\Pi_{(1,0)},\Pi_{12500}=\Pi_{(5,4)}$。
上表逐系数给两个完整新身份
$$
 \boxed{
 H_{125}-\frac{11}{37800}F_{11,125}
     =\frac1{270}F_{10,125}
     =\frac{\delta}{2721600}\Delta_{125},}
 \tag{38}
$$
$$
 \boxed{
 H_{12500}-\frac{11}{23625}F_{11,12500}
     =\frac{\delta}{1701000}\Delta_{12500}\ne0.}
 \tag{39}
$$
抵消的是这些实际块的完整质量；右边的完整函数而非仅质量或首项也
已经由两个 raw pull 系数确定。两个比率不同，不可拿一个常数
同时消去两块，更不能将全 $H$ 与全 $F_{11}$ 之差统称为某一条旧差。

在共同 $b=17$ 中，(38)–(39) 的右边各另乘 $17^{-1}$。
所以在 R968 指数 $(p-1)v$ 的原 ordinary 权变量下，两条旧差的导数分别为
$$
 \frac{\delta}{17\cdot2721600}(p-1)
       \log_p\langle\pi/\bar\pi\rangle(1-\upsilon_p),\qquad
 \frac{\delta}{17\cdot1701000}(p-1)
       \log_p\langle\pi/\bar\pi\rangle(1-\upsilon_p),
 \tag{40}
$$
均非零。原惰性 charge130 Newton 导数相应为
$$
 \frac{\delta}{17\cdot2721600}(p+1)\log_p(\pi/\bar\pi),\qquad
 \frac{\delta}{17\cdot1701000}(p+1)\log_p(\pi/\bar\pi),
 \tag{41}
$$
也均非零。这里没有给 $H_d$ 或 $F_{11,d}$ 单独的中央导数赋零；
它们原本的 primitive 导数项仍按 (27) 保留，只有所示真实质量抵消
使那一项准确相消。

v7 还明确返回：减去两old块后的 $F_{10}$ 完整余项确在原
$E_{65^3}$ 线上；对 $F_{11}$ 作同样操作，余项**不**只在
$E_{260}$ 线上。后者全余项摘要为
84daf3237cb7469f278e92b777dd21daf33ebe9e8a58c600d583ec280ea611ff。
这是保留其其他 primitive 及非六次部分的实际检查。

## 原输入与复核路径

- R297/R732 的原 norm13 完整 division 比，给 (4)–(6)；
  本篇 (7) 自行保全部幂和规范。
- R973：degree130 的全部有限类型，两个13-old的实际全局角色，
  完整质量列及其余块的算术范围。
- R971/R976：实际 $F_{10}$ 全来源、全部81投影、(14) 的唯一旧余项。
- R968/R410：同一 ordinary 射线、整个 $\mathcal S_{10}$ 的绝对核，
  真实单位切域与 $1\pm\lambda_p$ 的单位性。
- R301/R970：同一 Gaussian 的完整受限 Newton 构造和全整数特化；
  本篇 (30)–(34) 是两个旧退化之间的新精确比较。
- scripts/check-original-degree130-old-thirteen-source.py：
  从同次全390生产器限制到22列，现造 (7) 的全部四列，
  全回乘下推两个好位至 $V_{10}$，读取两条真实 primitive 线并
  核其两pull张成整个旧块；逐项返回 $F_{10},F_{11},\mathscr H_{130}$
  的两pull系数及质量，不把生成矩阵或坐标表作为输入。
