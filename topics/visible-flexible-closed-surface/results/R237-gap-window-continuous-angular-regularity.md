# R237：准确 Γ95 前缀与 own-zero 后段的整窗角正规性

日期：2026-11-26。会话：Astra-visible-flex-6a65e705。

本条支付新 gap $1.05$ 全场供应器中此前未付的一个具体缺口：完整 Hermite 短窗的角速度在**整个物理窗口和全部材料角**上有严格正下界，故其准确自然周长角反参确实存在，且保持两端完整位置两 jets。证明消费 R231–R233 的准确前缀，另对同一 Γ95 的准确 coast 出口进行 2048 个完整角盒的整数区间计算；没有把有限角样本最小值或 `minImmersion` 当作证明。

范围是准确积分、准确相同端函数的数学供应器，配合下述明确 own-zero Cauchy 状态。literal 浮点求积、角反参和物理端点舍入的完整误差尚未支付；本条也不覆盖后来加入 Cartesian 修正的场。

## 1. 对象、结论和准确定义

原 own-zero INITIAL 的 SHA 为

`1e3ae25e984fd4ac166022644cb5cbc248976e749ca391859d08ac1d45a7aced`。

其 1788 个有限参数中，除 cut-height 第 874 列及真实 tail 振幅第 1787 列外，其余值均严格为零；本条程序实际核对此事实。尾振幅为 $.8746432018013935<7/8$，真实 cuff 高度为 $.51$。它不是 long CI 的非零状态，也不是接口 probe。

中央两个椭圆的输入轴为

$$
(A_o,B_o)=(1.4360242681433948,.4360242681433949),\qquad
(A_n,B_n)=(1.4532280772048913,.4032280772048914).
$$

各已保存 binary64 数在本条准确定义中取其精确二进有理值。取 $c=13/128$，ramp 长度为保存的 $.06$，coast 长度为保存的 $.02$，新坡度为保存的 $.045$；准确 $b$ 定义为这三个长度的**实数和**，而非另外把相加结果重新舍入。$h$ 为保存的 $.2$。原后段参数及 $S=.9772364498716914$ 按已绑定 source 的准确形式使用。程序在报告中逐项输出准确有理 $c,b,h,b+h,S$；此处短十进制仅用于辨认。

令 $X_o(s,u)$ 为该 own-zero 源的准确形式，令 $X_n$ 为 R233 准确归一化 ramp 及其同一准确 Γ95 coast。其自然材料角一致。定义在 $s=b$ 的完整端函数差

$$
P(u)=X_n-X_o,\qquad V(u)=X_{n,s}-X_{o,s},\qquad A_2(u)=X_{n,ss}-X_{o,ss}.
$$

在 $t=(s-b)/h\in[0,1]$ 上定义

$$
Y(s,u)=X_o(s,u)+H_0(t)P(u)+hH_1(t)V(u)+h^2H_2(t)A_2(u),
$$

其中

$$
H_0=(1-t)^3(1+3t+6t^2),\quad
H_1=t(1-t)^3(1+3t),\quad
H_2=\tfrac12t^2(1-t)^3.
$$

这就是已实现短窗的准确数学定义；它在 $b$ 与新 coast 匹配完整位置两 jets，在 $b+h$ 与旧源匹配完整位置两 jets。

**结论。** 对所有 $(s,u)\in[b,b+h]\times\mathbb S^1$，

$$
|Y_u(s,u)|\ge
\frac{8115655028744818296304858287}{19807040628566084398385987584}
>.4097.
\tag{1}
$$

因此

$$
a_Y(s)=\frac1{2\pi}\int_0^{2\pi}|Y_u(s,v)|\,dv,
\qquad
\int_0^{v(s,u)}|Y_u(s,w)|\,dw=a_Y(s)u
\tag{2}
$$

定义了正的 $C^2$ 自然半径及 $C^2$ 的圆周定向保留角反参。$\widetilde X(s,u)=Y(s,v(s,u))$ 满足 $|\widetilde X_u|=a_Y(s)$，并保持两个接口的完整位置两 jets。只支付 $G=a_Y^2$ 及角正规性，尚未支付 $E=1,F=0$；特别地，(1) 本身不能证明 $X_s,X_u$ 线性无关。

## 2. Hermite 预算将整窗化为三个全角端函数界

直接求导可得准确最大值

$$
\|H_0\|_\infty=1,\qquad
\|H_1\|_\infty=16/81,\qquad
\|H_2\|_\infty=54/3125.
$$

后两个最大值分别在 $t=1/3,2/5$。于是

$$
|Y_u-X_{o,u}|\le P_*+h\frac{16}{81}V_*+h^2\frac{54}{3125}A_*.
\tag{3}
$$

这里需要的是全角上界 $P_*\ge|P_u|$、$V_*\ge|V_u|$、$A_*\ge|(A_2)_u|$。本条实际得到

| 准确函数全角量 | 严格有理计算的十进制显示上界 |
|---|---:|
| $P_*$ | .427361740859861 |
| $V_*$ | 3.516051453803626 |
| $A_*$ | 34.71737913426213 |

显示位不作为比较依据。下文给出完整来源，最终判定使用报告里的有理数。

## 3. 两个中央椭圆的同材料角切向差

对轴 $(A,B)$ 记 $a=(2\pi)^{-1}\int|\Gamma_\theta|d\theta$。置 $C=(A+B)/2,z=(A-B)/(A+B)$，则

$$
|\Gamma_\theta|=C|1-ze^{2i\theta}|,
\qquad a=C\sum_{j=0}^{\infty}b_j^2,
$$

其中 $b_0=1$，$b_j=b_{j-1}z(2j-3)/(2j)$。这是 $(1-ze^{2i\theta})^{1/2}$ 的绝对收敛 Fourier 展开与其共轭相乘后的常数项。取前 64 项，尾部严格不超过

$$
\frac{C b_{65}^2}{1-z^2}.
$$

全部乘除和平方根按 96-bit 整数区间向外舍入，实际得到 $a_o,a_n>1$，且

$$
|a_n-a_o|<1.937\times10^{-17}
$$

的有理包含；未使用椭圆周长浮点求积。准确归一化材料角的导数密度差受

$$
M\le\frac{\max(|A_n-A_o|,|B_n-B_o|)}{\min(a_o,a_n)}
+\frac{A_o|a_n-a_o|}{a_na_o}
$$

控制，实际有理上界显示为 $.03266283387845565$。两个材料角映射在每个象限端点都等于同一 $j\pi/2$；差函数在象限两端为零且导数不超过 $M$，因此其绝对值不超过 $\pi M/4$，显示为 $.02565332973949502$。

固定原生椭圆角时，沿两轴线性路径正规化切向，可用

$$
\frac{|A_oB_n-B_oA_n|}{2\min(A_o,A_n)\min(B_o,B_n)}
$$

控制单位切向差。这来自 $|\sin\theta\cos\theta|/(A^2\sin^2\theta+B^2\cos^2\theta)\le1/(2AB)$。旧椭圆按归一材料角的单位切向导数不超过 $a_oA_o/B_o^2$。两项相加给同一材料角的中央切向差

$$
\sup_u|T_n(c,u)-T_o(c,u)|\le C_T,
\qquad C_T<.241704412
\tag{4}
$$

的严格有理包含。未把两组椭圆的不同原生角误认为同一材料角。

## 4. 新前缀的真实材料切向输运

对 R233 的 raw ramp 场记 $q=|Y_\theta|$。经其准确中心缩放、角反参后，单位角切向仍为 $T=Y_\theta/q$，只是要在 $s$ 依赖的 $\theta(s,u)$ 处取值。令 R231/R233 已支付的真正去均值角 primitive 控制 $q|\theta_s|\le W$，并写 $q_s/q=f_s/f+e/q$。则

$$
|T_s|\le\frac{|Y_{s\theta}|}{q}+\frac{|f_s|}{f}
+\frac{|e|}{q}+\frac{2|Y_{\theta\theta}|W}{q^2}.
\tag{5}
$$

最后一项由 $|T_\theta|\le2|Y_{\theta\theta}|/q$ 得到，不能删掉 $s$ 依赖角逆项。缩放因子对单位切向本身消去，故这里没有遗漏其径向导数。

本条消费前 15 格以及最后一格的**全部**已证范数和 primitive，保留已证高频加权尾；实际使用

$$
q>.403,\quad |Y_{s\theta}|< .462576157,\quad
|Y_{\theta\theta}|<1.885495991,
$$

以及 $|e|<1.823\times10^{-7}$、$W<8.198\times10^{-8}$ 的有理包含。$q>.403$ 由全 16 格 raw Gram 误差和 $B_n$ 的准确值核实；所有短十进制显示均不代替有理判定。代入 (5) 得

$$
|T_s|_{\rm ramp}<1.192651029.
$$

在准确 R137 coast 上 $T_s=mN$。第二基本形式秩一且非零主曲率为 $\lambda$ 时 $|m|\le|\lambda|/2$。消费 R232 的**全 coast** 上界 $|\lambda|<8.893$，并实际核对其证书标记及有理值，而非拿仅出口的上界代替整段。因此

$$
\sup_u|T_n(b,u)-T_n(c,u)|
\le r\,C_{Ts}+L_c\,8.893/2=:C_{\rm pre}<.160489062
\tag{6}
$$

有严格有理版本，其中 $C_{Ts}$ 是报告中的完整有理 ramp 上界。这里 $r,L_c$ 是准确二进有理 ramp/coast 长度。

## 5. 同一准确 Γ95 coast 的全角出口导数

本条新计算准确付清 $|X_{n,su}(b,u)|$ 及 $|X_{n,ssu}(b,u)|$，不是把旧样本端迹差当上界。

使用 R233 的完整 95 阶实 Fourier 曲线 $\Gamma$；原保存复系数经真实共轭配对取实函数，未强行过滤微小奇偶模。准确原周长半径 $a_\Gamma$ 及目标准确入口半径 $f_0$ 使用 R233 的有理盒。原生角速度为 $q_\Gamma$，则入口材料导数为 $D_u=(a_\Gamma/q_\Gamma)D_\theta$。

入口单位角切向为 $T$，令 $U=T_u/|T_u|$，

$$
d=-\frac{v}{|T_u|}U+\sqrt{1-\frac{v^2}{|T_u|^2}}\,(T\times U),\qquad N=d\times T.
$$

取 $n=T_u\cdot N/f_0$、$m=d_u\cdot N/f_0$、$k=m/n$。沿既有 R137 准确 ruled 延拓，在 $\sigma=L_c$ 处置

$$
\begin{aligned}
r_0&=f_0/v,& r&=r_0+L_c,&\Delta&=L_c(2r_0+L_c),\\
w&=\frac{\Delta}{r_0+\sqrt{r_0^2+(1+k^2)\Delta}},&
A_r&=r_0+(1+k^2)w,&
D&=f_0+w\{v(1+k^2)-k_u\},\\
U_t&=D/(vA_r),& k_e&=kr_0/A_r,&
\lambda&=f_0n(1+k^2)/D.
\end{aligned}
$$

令 $c_r=r_0+w,b_r=kw$，则真实出口两 frame 及径向加速度为

$$
X_s=\frac{c_rd-b_rT}{r},\qquad
T_e=\frac{b_rd+c_rT}{r},\qquad
X_{ss}=\frac{\lambda k_e^2}{1+k_e^2}N.
\tag{7}
$$

真实出口材料角导数是

$$
D_{u_e}=\frac{a_\Gamma/q_\Gamma}{U_t}D_\theta.
\tag{8}
$$

程序对 (7) 用 (8) 作区间 Taylor jet 自动微分，不数值求任何角反参。按 $2048$ 个完整原生角盒覆盖圆周，使用 Fourier 各阶完整绝对和的 Taylor 余项；整数精度为 96 bit，最高输入角导数阶数 11，实际 series 阶数 8。每盒都核实 $n>0$、ruling 根号正、$D>0,U_t>0$，因此所有除法合法。该新计算较松的完整出口域下界仍为 $D>.9078,U_t>.9019$。

最终全角严格界为

$$
|X_{n,su}(b,u)|\le
\frac{210850661771019569642660284453}{79228162514264337593543950336}
\quad(\text{显示 }2.6613095025781743),
$$

$$
|X_{n,ssu}(b,u)|\le
\frac{1208960937480437650168291944147}{79228162514264337593543950336}
\quad(\text{显示 }15.259232312282577).
\tag{9}
$$

全 2048 盒的整数标量行 hash 为

`584b9c0c14ccdeb6b9b5a5b7044744f225970d2e27a972b40c0bf00b2d739da4`。

这一步没有重复登记 R137 的机制，也没有把数值 Fourier 近似当作未绑定的新曲线；它消费已冻结的同一 Γ95 准确函数，付清先前未付的实际出口混合导数。

## 6. 原 own-zero 源的全角端口界

所有自由角系数为零是本节的实质输入。原完整参考在 $b$ 的球面单位切向由中央椭圆切向 $T_o$ 和圆切向 $e$ 构成：

$$
T_{\rm raw}=\big((1-q_w)e+q_wT_o,\ r_w H\big),\quad
q_w=\frac{1+\cos(\pi\chi)}2,\quad r_w=\frac{\sin(\pi\chi)}2,
$$

$$
\chi=S_5\!\left(\frac{s-c}{S-c}\right),\qquad
H=2\sin\frac{\arg T_o-\arg e}{2}.
$$

两个平面切向处于同一象限，故 $|H|\le\sqrt2$；$r_w^2=q_w(1-q_w)$ 保证单位长度。令 $c_p^2=1-2r_w^2$ 作为平面长度平方的下界。再加上 R205 的 $\chi$ 倍 tail 方位/极角。原 raw 极角关于 $u\mapsto\pi-u$ 奇对称；本条在整窗实际证明

$$
|\phi_{\rm raw}|< .791163754<\pi/2.
$$

故准确半周期平均的虚部为零、实部为正，平均相位及其前两个径向导数均为零。这是准确对称公式的结论，不是对 literal quadrature 数值假设对称，也不适用于一般非零 CI 状态。

记真实尾振幅为 $A_t$，$C=\cos A_t>0$，取

$$
B_0=\frac{1-C}{2\sqrt C}+A_t.
$$

它控制 tail 方位角变化与极角的绝对值之和。因为 tail 平面切向分母不小于 $C$，对其 `atan2`/极角公式微分可取

$$
B_1=2\alpha_s^*/C,\qquad
B_2=2(\alpha_{ss}^*+(\alpha_s^*)^2)/C+3(\alpha_s^*)^2/C^2.
$$

在本端口 $a_s=.05,a_{ss}=0$，R205 的 $S_9$ 导数给

$$
\alpha_s^*\le\frac{A_t}{.46}\frac{630}{256}(.05),\qquad
\alpha_{ss}^*\le\frac{A_t}{.46^2}\frac{2520}{64}(.05)^2.
$$

若 $A_s=|\theta_s|+|\phi_s|$、$A_{ss}=|\theta_{ss}|+|\phi_{ss}|$，对 raw 参考的平面角和极角直接微分，再加上述 tail 部分，可取

$$
\begin{aligned}
A_{s,0}&=\sqrt2(|q_{w,s}|+|r_{w,s}|)/c_p,\\
A_{ss,0}&=\sqrt2(|q_{w,ss}|+|r_{w,ss}|)/c_p
+2(\sqrt2q_{w,s}/c_p)^2+2|q_{w,s}r_{w,s}|/c_p^2,\\
A_s&\le A_{s,0}+|\chi_s|B_0+\chi B_1,\\
A_{ss}&\le A_{ss,0}+|\chi_{ss}|B_0+2|\chi_s|B_1+\chi B_2.
\end{aligned}
\tag{10}
$$

所有球面两角图的混合偏导向量范数均不超过 1，故

$$
|T_s|\le A_s,\qquad |T_{ss}|\le A_{ss}+A_s^2.
$$

实际有理结果显示为 $A_s< .799479110$、$A_{ss}<18.612302759$。由 $X_{o,u}=f_oT$ 得

$$
|X_{o,su}(b,u)|< .854741952,\qquad
|X_{o,ssu}(b,u)|<19.458146822.
\tag{11}
$$

同一参考还满足

$$
|T_o(b,u)-T_o(c,u)|
\le\sqrt2(|1-q_w|+|r_w|)+\chi B_0
=:C_{\rm old}<.022125048.
\tag{12}
$$

此时 $\chi(b)$ 的显示值为 $.006618317963975396$，$c_p>0$ 由有理盒核实。

令准确出口半径

$$
f_n=a_n+v_nr/2+v_nL_c,\qquad
f_o=a_{o,\mathrm{base}}+v_or/2+v_oL_c.
$$

注意 $a_{o,\mathrm{base}}$ 是所绑定原 scalar base 的保存参数，不把它暗换成新求得的椭圆积分。由 (4)、(6)、(12)，

$$
|P_u|=|f_nT_n(b,u)-f_oT_o(b,u)|
\le|f_n-f_o|+f_o(C_T+C_{\rm pre}+C_{\rm old}).
$$

程序用这三项的完整有理数给出第 2 节的 $P_*$；由 (9)、(11) 分别相加给出 $V_*,A_*$。因此三个端函数界全部来自全角解析或区间证明。

## 7. 整窗旧半径与最终正下界

原 scalar right 段长度为 $.7956739498716915$，采用已冻结 power $7$ 以及明确 $\beta\in[0,1]$：

$$
f_o'(s)=v_o-(1+v_o)\{(1-\beta)S_9(x)^7+\beta S_9(x)^8\},
\qquad x=(s-b)/L_{\rm right}.
$$

在本短窗 $0\le x\le h/L_{\rm right}$，$S_9$ 单调且小于 1，所以

$$
f_o'(s)\ge v_o-(1+v_o)S_9(h/L_{\rm right})^7>.049999999>0.
$$

准确 $f_o(b)>1$ 已由源参数及有理预算核实。因此整窗 $|X_{o,u}|=f_o(s)>1$。将三个严格有理端函数界代入 (3)，实际得到

$$
|Y_u-X_{o,u}|\le
\frac{11691385599821266102081129297}{19807040628566084398385987584}.
$$

从 $|Y_u|\ge|X_{o,u}|-|Y_u-X_{o,u}|$ 立刻得到 (1)。这里没有对 $s$ 或 $u$ 采样，也没有把小角速度下界冒充二维面积下界。

## 8. 准确角反参及完整两 jet 接缝

正下界 (1) 允许对 (2) 应用隐函数定理，并给 $v_u=a_Y/|Y_u|>0$。所有输入端函数角向光滑，且 $Y,Y_s,Y_{ss}$ 在两个接口分别等于对应准确源的同一全角函数。两个源在接口邻域已按各自自然材料角满足 $|X_u|=a(s)$，所以接口的 $q,q_s,q_{ss}$ 皆与 $u$ 无关。对 (2) 连续微分，得到接口上

$$
v=u,\quad v_u=1,\quad v_s=v_{ss}=v_{su}=v_{uu}=0.
$$

因此完整链式法则给 $\widetilde X$ 与各端源的 $X,X_s,X_u,X_{ss},X_{su},X_{uu}$ 全部一致。没有以只接位置或只接度量替代位置两 jets。准确新自然半径也在两个接口保持其完整二阶端迹。

这不表示角反参自动消去 $E,F$，也不表示 $Y$ 或 $\widetilde X$ 已嵌入。尤其后续 Cartesian 修正一般改变 $G$，其角正规性和二维浸入需要各自重新支付。

## 9. 实际执行、源身份与边界

准确出口脚本 `6a65-geometry-coast-outlet-derivative-bounds.py`，SHA：

`410b02e69131b686362a8c14cae529e41254fea7c0f051bd288d27a6434e92bc`。

整窗脚本 `6a65-geometry-gap-window-angular-regularity.py`，SHA：

`fc61e30afacb391aeff61c02258a0c6de11fabdaa4e5f189067e0a24a7af5b06`。

出口脚本的 2048 盒运行自然 `exit 0`，外部实测 $43.037119848$ 秒、RSS $26880$ KiB。整窗最终带完整 coast 身份核验的运行自然 `exit 0`，实测 $.211071656$ 秒、RSS $24620$ KiB。

| 本地实际原件 | SHA-256 |
|---|---|
| 同一 Γ95 coast master | `f2c834f5b2b9d1471eabb64a3be0edcc7b6f8454f8c98d68793a60c782c46b4d` |
| 同一 ramp master | `0e2865ed7fd2fa5e1061718cc96b8be691f5f7d1a5b9460cf11d564d799f38e7` |
| R233 terminal primitive 报告 | `23fd5b56609e5b35725758a5a822ce893e61c6b8204db7b3e29ef592ba221b0f` |
| R233 最后格报告 | `9e16f7da5211c425b1fb8d6414e521c99f57d40f7c5cdf8b465a55b974c1ad24` |
| R232 全 coast 报告 | `88b4cc19139143fdb1e85f446750f3daea70d978a139171702bb3fe6381adc89` |
| `gap105-coast-outlet-derivative01-report.json` | `ec0e8c0de4d2841fbb5775990cff71838f806ed776c0fbd4b3a8ba1e3cebe295` |
| `gap105-window-angular-regularity03-report.json` | `9835a317dd9bc670b99ce026c485f17044b6de231c05c0b1fb855ac635023c0e` |
| 出口实际日志 | `9f23a9933ffc9e921403a23c237a71b37df8a7edff57ca164db89d84d33f6f08` |
| 整窗最终实际日志 | `0cd9cb9b26d43247b6778ff6c3f93d7c616345b0673b5b34ca0acf851eb05385` |

复生时先按 R231–R233 及 own-zero 源记录生成上述同身份输入；出口程序使用 --scripts、--port-source、--port-report、--coast-master、--cells 2048 和全新 --output，整窗程序使用 --scripts、--work 和全新 --output。两个程序均拒绝覆盖已有报告，输入身份不符即退出。

实际区间 helper 为已公开 `6a65-m12-r137-continuous-domain.py`，SHA `6bc46eeeb91bb979c19c2167250ced2a8362ae92b8f8b53eacd8595408e2af57`；全 Fourier/Taylor jet 源为 R232 的 `6a65-geometry-final-ramp-port-certificate.py`，SHA `0cfe24c3be23e90986345119bac15c65a018aeaa9ba909318b9bbcb4d06ddc90`。准确常数中心 $C_\Gamma$ 沿 R232 定义取 Γ 的 Fourier 常数项；它不是全 ramp 归一化使用的弧长加权中心。

第一次整窗接口运行因写错既有最后格报告 hash 而在计算前退出 1，保留该失败原件；纠正为真实已发布 hash 后运行通过，最终第 03 次另外显式核验并记录 R232 全 coast 身份。未改准确输入或转借旧通过记录。原始大数组、checkpoint、运行 JSON 不公开上传，本条公开完整数学定义、证明、可复生程序和实际标量身份。

本条支付准确形式整窗 $G$ 的定义和角反参两 jet 接口。literal 浮点消费者到准确形式的全 $C^2$ 误差、整窗二维浸入、全核等距、所有非局部 reach、held 和同一 $g$ 的跨时族均未由本条推出；这些继续在完整几何源及全参数求解中实付。
