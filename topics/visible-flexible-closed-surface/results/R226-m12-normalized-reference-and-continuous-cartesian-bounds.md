# R226：M12 准确中央归一参考的全时几何与全半体 Cartesian 连续修正界

2026-11-26，Astra-visible-flex-6a65 / g5-and-exact。

**状态：下述确定参考族的连续度量、全时嵌入、reach、held 与含反射非全等已证明；整数区间及有理预算实际 exit 0。另给任意已保存全半体 B-spline 修正的连续六 jet 上界算法。尚未把未收到的 solver field 的数值或几何归入本结果。**

这里处理原同一 M12 度量。参考改变正是当前 common-cut / entire-half Cartesian 求解器已有的中央准确曲线与两 jet 修正；不是另外改变目标度量，也不是将 R114 的同像材料修复误当本参考。

## 1. 唯一参考及结论

令 $X_\alpha$ 为 [R21](R21-m12-whole-map-and-actual-metric-decrease.md) 的准确 common-cut 闭族，沿用其固定度量 $g$、两帽、相位区间 $0\le\alpha\le2\pi/3$。其定义由原 prefix payload、准确 common-cut metadata、准确桥证书及原有限尾清单绑定；本文不改它们。

在上半体中央，原 native 平面曲线为有限 Fourier 曲线 $\gamma(\psi)$。它的系数按原二进数据的准确有理数解释。记

$$
J=|\gamma'|,\qquad a=\frac1{2\pi}\int_0^{2\pi}J(\theta)\,d\theta,
\qquad U(\psi)=\psi-\frac{e_0}{3}\sin(3\psi),\qquad \rho=U'=1-e_0\cos(3\psi).
$$

旧中央的均值高度为零。定义新的 degree-one 弧长角

$$
U_0(\theta)=\frac1a\int_0^\theta J(v)\,dv,
\qquad \theta=U_0^{-1}(u),\quad \psi=U^{-1}(u).
$$

新的中央两 jet 为

$$
\Gamma(u)=\gamma(\theta)/a,\qquad X_s=e_z,\qquad X_{ss}=0.
$$

这里 $s$ 是原目标度量的物理经线弧长，native 坐标等于 $\lambda s$；$\lambda$ 是原准确桥定义的比例，不能换成 $1$。令 $h=T_u\varepsilon$ 为原首 ramp 的完整物理长度，约 $.284488$。取原中央与新中央之差为 $\Delta_j(u)$，$j=0,1,2$。在 $0\le s\le h$ 定义

$$
C(s,u)=H_0(s)\Delta_0(u)+H_1(s)\Delta_1(u)+H_2(s)\Delta_2(u),
$$

其中 $H_j$ 是在 $s=0$ 支付第 $j$ 阶单位迹、在 $s=h$ 三条迹全零的五次 Hermite 基。在 $s\ge h$ 令 $C=0$。下半体取原完整镜像；帽保持原样。记修正后的参考族为 $\bar X_\alpha$，直径为 $\bar D$。

**结论。** $\bar X_\alpha$ 为 $C^2$ 拓扑连续的连通闭 $C^2$ 嵌入族，原同一固定帽集合 $H$ 满足

$$
\sup_{\alpha,p}\|g^{-1/2}(\bar X_\alpha^*e-g)g^{-1/2}\|_{\rm op}
<7.667\cdot10^{-8}<10^{-6},
$$

$$
\frac{\operatorname{reach}(\bar X_\alpha(M))}{\bar D}>.03120330,
\qquad \frac{\delta_{\rm hold}}{\bar D}>.05278322,
\qquad \frac{\operatorname{diam}\bar X_0(H)}{\bar D}>.93,
\qquad \delta_E>0.
$$

这项确定参考的连续证书保证后续 solver 的基线身份及几何预算。它不证明精确等距，也不把粗三角界当实际求解残差或 README 第 5 条的收敛结果。

## 2. 先相减再积分：严格中央弧长与累计角

原曲线是平面的。写其复坐标为

$$
\gamma_x+i\gamma_y=\sum_m c_m e^{im\psi},\qquad c_m\in\mathbb Q,
\qquad m\equiv1\pmod3.
$$

准确源给出 $J\ge J_*>.198798659$。此下界直接来自频率 $1$ 项与其余一阶项的反三角不等式。定义小的准确三角多项式

$$
D=J^2-\rho^2=\sum_k d_k e^{ik\psi}.
$$

系数先按 Fraction 完全相减。实际绝对和为

$$
\sum_k|d_k|<1.022829\cdot10^{-9},\qquad
\sum_k|k d_k|<3.893820\cdot10^{-8}.
$$

不分别积分两项很大的 $J$ 和 $\rho$。令 $L=J-\rho$，则

$$
L=\frac{D}{J+\rho},\qquad 2\rho L+L^2=D.
$$

设 $D_n=\sum_k|k|^n|d_k|$、$\rho_*=1-|e_0|>0$，取

$$
B_0=\frac{D_0}{J_*+\rho_*}.
$$

对 $1\le n\le4$，从最后的恒等式逐项微分，两个最高阶项合成 $2J L^{(n)}$，得到严格递推上界

$$
B_n=\frac{D_n+
2\sum_{k=1}^{n}\binom nk3^k|e_0|B_{n-k}
+\sum_{k=1}^{n-1}\binom nk B_kB_{n-k}}{2J_*}.
\tag{1}
$$

所以 $|L^{(n)}|\le B_n$。当前准确输入给 $B_4<.026766669$。

在 2048 个等角 panel 上使用中点 Simpson。每个 panel 的角宽记为 $b$，该 panel 的完整误差不超过 $b^5B_4/2880$。所有函数值由既有 96-bit 整数区间工具计算：Machin 公式包住 $\pi$，带明确余项的 Taylor 多项式包住三角函数，整数平方根包住 $J$。全过程没有把浮点三角值或 Gauss 差值充当包围。

完整 $\int L$ 的 Simpson 余项小于 $5.174\cdot10^{-15}$。实际所得准确包围为

$$
\frac{19807040628565953354573449137}{19807040628566084398385987584}
\le a\le
\frac{39614081257131971944208347971}{39614081257132168796771975168}.
\tag{2}
$$

尤其 $1-7\cdot10^{-15}<a<1-4\cdot10^{-15}$。

对于每一个 panel 端点，同时累计之前的 Simpson 项及其全部余项。由

$$
U_0(\theta)-U(\theta)
=\frac{\int_0^\theta L(v)\,dv-(a-1)U(\theta)}a
\tag{3}
$$

得所有端点的区间。区间内部使用

$$
|(U_0-U)'|\le\frac{B_0+|a-1|(1+|e_0|)}{a_-}
$$

及到最近 panel 端点的距离至多 $b/2$。这一步覆盖完整角域，不是只保留有限节点结果。再用 $U^{-1}$ 的 Lipschitz 常数 $1/\rho_*$，得到

$$
|\theta(u)-\psi(u)|<1.267334\cdot10^{-10}.
\tag{4}
$$

全部点区间行的 SHA256 为 `76d039d98b02389175f62f5dc9ee96b41bdbb77f81e1947666564ab0eefa88e3`；行流可重算，不保存大表。

## 3. 中央完整两 jet 的差

设 $G_j=\sum_m|m|^j|c_m|$，它控制 $|\gamma^{(j)}|$。记 $T=\gamma'/J$、$A=T'/J$，则

$$
|T'|\le G_2/J_*,\qquad |A|\le G_2/J_*^2,\qquad
|A'|\le2G_3/J_*^2+7G_2^2/J_*^3.
\tag{5}
$$

最后一式直接微分 $A=\gamma''/J^2-\gamma'J'/J^3$，使用 $|J'|\le G_2$、$|J''|\le G_3+G_2^2/J_*$。

令 $v=J/\rho$。旧中央曲线在 $u$ 下的速度为 $vT$，新归一曲线的速度为 $T$。因此

$$
(\Delta_0)_u=T(\theta)-v(\psi)T(\psi),
$$

$$
(\Delta_0)_{uu}
=a[A(\theta)-A(\psi)]+[a-v(\psi)^2]A(\psi)
-T(\psi)\frac{v'(\psi)}{\rho(\psi)}.
\tag{6}
$$

这里 $v^2=1+D/\rho^2$，所以 $v'$ 由同一准确 $D,D'$ 控制；未用两个大切向量分别取绝对值后相加。式 (2)、(4)—(6) 给 $\Delta_0$ 的完整 $u$ 两 jets。

原 native 中央一阶位置迹准确为 $e_z$，原 chart 的一阶径向导数准确为零。因此

$$
\Delta_1=(1-\lambda)e_z,
\tag{7}
$$

并从原准确桥根盒计算 $\lambda$ 的上下界，未把这个差设为零。

设 $Q(\psi)$ 为原 native 中央 Cartesian 二阶径向迹，$e''$ 为原 chart 的准确 native 二阶导数。旧材料二阶位置迹为

$$
(X_{ss})_{s=0}=\lambda^2\frac{P(\psi)}{\rho(\psi)},\qquad
P=\rho Q+\frac{e''}{3}\sin(3\psi)\gamma'(\psi).
\tag{8}
$$

这里的 $P$ 再次先按准确 Fourier 系数相减。其零、一、二阶系数绝对和分别小于

$$
1.194261\cdot10^{-9},\quad4.538068\cdot10^{-8},\quad1.728162\cdot10^{-6}.
$$

于是 $\Delta_2=-X_{ss}$ 及其两个 $u$ 导数由商的完整微分得到。例如若上述三项记 $P_0,P_1,P_2$，$r_1=3|e_0|,r_2=9|e_0|$，则

$$
|(\Delta_2)_{uu}|
\le\lambda_+^2\left(\frac{P_2}{\rho_*^3}
+\frac{3P_1r_1+P_0r_2}{\rho_*^4}
+\frac{3P_0r_1^2}{\rho_*^5}\right).
\tag{9}
$$

这包含原曲线归一、原两 jet 以及准确桥比例的全部差。

## 4. 首 ramp 的连续六 jets 和旧实际图的二阶界

三条 $H_j$ 的 Bernstein 控制点分别为

$$
(1,1,1,0,0,0),\quad(0,h/5,2h/5,0,0,0),\quad(0,0,h^2/20,0,0,0).
$$

它们及物理 $s$ 导数的绝对上界矩阵为

$$
\begin{pmatrix}
1&2h/5&h^2/20\\
5/h&2&h/4\\
20/h^2&12/h&2
\end{pmatrix}.
\tag{10}
$$

将第 3 节的准确迹界乘入 (10)，得到整个首 ramp 的连续上界：

| 量 | 保守向外十进制上界 |
|---|---:|
| $|C|$ | $2.525\cdot10^{-10}$ |
| $|C_s|$ | $4.437\cdot10^{-9}$ |
| $|C_u|$ | $2.104\cdot10^{-8}$ |
| $|C_{ss}|$ | $6.836\cdot10^{-8}$ |
| $|C_{su}|$ | $3.698\cdot10^{-7}$ |
| $|C_{uu}|$ | $9.526\cdot10^{-6}$ |

曲率传递还须支付旧实际 $X$ 的二阶坐标导数。复用 R216 的准确 Hermite cell 系数转换，对整个修正支撑相交的 **501 个原 source cells** 全部取导数系数界；chart 的 **10 个完整 cubic pieces** 用 Bernstein 控制点包住。common-cut 后段修正不在本支撑内。所有物理 $\lambda$ 因子照原桥盒保留。

得到 native 的 $|X_\psi|,|X_{ss}|,|X_{s\psi}|,|X_{\psi\psi}|$ 上界依次为

$$
2.601649433,\quad3.627644081,\quad2.361400702,\quad7.412300767,
$$

以及 $|e|<.800000000000001$、$|e'|<1.156886423$、$|e''|<6.953007761$。用 R216 已列完整隐函数两 jet 公式，且本支撑上 $f\ge1$，得到

$$
C_X:=|X_{ss}|+2|X_{su}|/f+|X_{uu}|/f^2<2129.329705.
\tag{11}
$$

这不是曲率换名、不是节点二阶导数最大值；它确实覆盖原位置图各 source cell 内部、chart 拼缝与整个修正区。

## 5. 原全时几何的实际传递

采用 R21 的 $d=2.57212\cdot10^{-8}$，并用第 4 节尚未向十进制截断的准确有理界定义

$$
\eta=\|C\|_\infty,\quad
p=\|C_s\|_\infty+\|C_u\|_\infty,\quad
C_C=\|C_{ss}\|_\infty+2\|C_{su}\|_\infty+\|C_{uu}\|_\infty.
$$

本支撑 $f\ge1$，所以 $p$ 控制 $dC$ 的目标正交标架算子范数。R216 的准确恒等式及法向归一化估计给

$$
d_1=d+2(1+d)p+p^2<7.667\cdot10^{-8},\qquad
\epsilon_n=\frac{3p+p^2}{1-d}<7.643\cdot10^{-8}.
$$

原此区实际主曲率小于 $5.547266$。由 (11) 及第二基本形式的完整差，

$$
K_1\le\frac{5.547266(1+d)+\epsilon_n C_X+C_C}{1-d_1}<5.547440.
\tag{12}
$$

未改的尾、圆领及帽保持旧结论，故整个新参考仍可取

$$
K=\frac{4763997235009095}{562949953421312}.
$$

令 $R=2131902881202937/1125899906842624$ 为 [R25](R25-m12-sharper-enclosing-ball.md) 的旧球界。正支撑满足

$$
(X+C)\cdot\bar n\ge .737-1.9\epsilon_n-\eta>.7369998>1/K.
$$

全部同伦 $X+vC$，$0\le v\le1$，满足相同界、同一 $C^2$ 镜像与帽接合。于是 [R10](R10-positive-support-offset-reach.md) 直接给闭嵌入及全点对 reach 至少 $1/K$；没有把局部曲率条件当非局部 reach 的替代。

新直径至多 $2(R+\eta)$，旧 held 见证至多损失 $2\eta$，固定帽完全不动。有理比较给

$$
\frac1{2K(R+\eta)}>.03120330,\qquad
\frac{.19989114-2\eta}{2(R+\eta)}>.05278322.
$$

含反射非全等也沿用 R216 对 [R16](R16-fixed-cap-volume-moment-noncongruence.md) 的完整调用。旧未标记实体面积小于 150，整条嵌入同伦把体积对称差限制在旧面的 $\eta$ 管内，故三阶复体积矩的改变量小于

$$
2400\eta(1+9\eta)^2<6.059\cdot10^{-7}.
$$

原活动矩实部大于 $.44016$，所以新值仍为正。原三重及镜面对称保持，固定凸起矩未改；三阶中心矩张量的范数在两个相位严格不同。它对含反射的全部 $E(3)$ 不变，因此 $\delta_E>0$。

最后，活动族仍是同一空间旋转与 uniform 材料角平移，后者保持原 $g$。所有全域上确界及几何界在该作用下不变，固定帽和中央镜像的两 jets 全时匹配。因此以上量词覆盖全部相位，不只若干样本时刻。

## 6. 已保存 solver field 的连续界：完整算法

这一节给可直接接下一次 whole-half cold job 的算法，不给尚未取得的 field 数字。由 [R223](R223-m12-common-chart-through-flat-cuff.md)，共同材料坐标为 $q=Tz$、$0\le z\le1$，真 cuff 是右端点，原 $r=.6$ cut 为内部。令 $H=ds/dq$。全背景旧证明给 $w\le16/15$、$|w_r|<24$；R223 的 polynomial chart 给

$$
H>.684,\qquad |H_q|<60.
\tag{13}
$$

后者由 $H=-r_q\sqrt{1+w^2}$ 微分，以及 $|R''|<3$、$h_{\rm tail}>.44$、$|r_q|<1.422$ 得出；程序执行准确有理比较。

设 $W(z,\theta)$ 为保存的 quintic B-spline / Cartesian Fourier 场。所有 binary64 系数、unit knots 按准确有理数解释。补回首尾各三个零控制行，则 $W,W_z,W_{zz}$ 在中央及真 cuff 准确为零。

若 degree 为 $p$，导数控制系数为

$$
c_i^{(1)}=p\frac{c_{i+1}-c_i}{t_{i+p+1}-t_{i+1}},
$$

去掉首尾各一个 knot 后继续同式得到二阶控制系数。对应 B-spline 非负且组成单位分割。因此对 $r+j\le2$，

$$
B_{rj}=\max_i\sum_k |k|^j|c_{ik}^{(r)}|
\quad\Longrightarrow\quad
|\partial_z^r\partial_\theta^jW|\le B_{rj}
\tag{14}
$$

在所有 cell 内部、节点及所有角度成立。水平复模与竖直 cosine 模都具有单位振幅；水平使用自己的实际频数 $1+3k$，不漏掉旋转标架频数。

原中央弧长图给 $|\theta_u|\le U_1=a_+/J_*$、$|\theta_{uu}|\le U_2=a_+^2G_2/J_*^3$。取原准确桥盒给出的 $T_->0$、$H_*=171/250$，完整物理 jets 满足

$$
|W_s|\le\frac{B_{10}}{T_-H_*},\quad |W_u|\le U_1B_{01},
$$

$$
|W_{ss}|\le\frac{B_{20}}{T_-^2H_*^2}+\frac{60B_{10}}{T_-H_*^3},\quad
|W_{su}|\le\frac{U_1B_{11}}{T_-H_*},\quad
|W_{uu}|\le U_1^2B_{02}+U_2B_{01}.
\tag{15}
$$

输出分别列出 solver 修正 $W$、确定参考差 $C$、以及相对于原 R21 图的总差 $C+W$，不得遗漏 $C$。全域 $f\ge r_{\rm cuff}$，而 $C$ 的支撑上 $f\ge1$，程序分别使用这两个半径界。

式 (14)—(15) 已是连续上界，不随观测点漏采而失效。对 $C+W$ 的新完整曲率仍需对应支撑上的原 $C_X$ 或完整 pullback connection；第 5 节只为 $C$ 支付了实际完整几何，没有提前借给未消费的全域 $W$。

## 7. 执行、来源与后续接口

证明及 checker：
[6a65-m12-entire-half-continuous-correction-bounds.py](../scripts/6a65-m12-entire-half-continuous-correction-bounds.py)。
它读取原 payload SHA256 `359d491cd592962d467fdd538013977ee9a92070346de41c227d9ca3e1ef3bd0`，原 common-cut metadata SHA256 `253179d585d4ac0e59206d4e579de5663943f126473668c45a3bbda665c9c8f2`，原 bridge SHA256 `1389cf1a339b0a0d749beb666b6def24a31e766eff0abf63289217728ceacdaa`。

实际参考证明命令为：

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python \
  topics/visible-flexible-closed-surface/scripts/6a65-m12-entire-half-continuous-correction-bounds.py \
  --reference-only \
  --data "$M12_COLD_DIR/m12-prefix-data.npz.gz" \
  --out "$M12_COLD_DIR/exact-normalized-reference-geometry.json"
```

该模式不读取、假设或冒充任何 solver field。新 field 的同 job 命令只把 `--reference-only` 换成

```bash
--field "$M12_COLD_DIR/entire-half/entire-half-result.json.field.npz" \
--grid "$M12_COLD_DIR/entire-half/entire-half-grid.json" \
--result "$M12_COLD_DIR/entire-half/entire-half-result.json"
```

并指定新的 `--out`。它核对真实 field/grid/result 的 SHA 后才消费系数。只发布小标量与 hash，原大数组保持 RUNNER_TEMP。

本次 `--reference-only` 自然 exit 0，9.058797071 s，全部 **10 项准确有理预算为真**。最终源码 SHA256 为 `81003432a6823b3c86859be226c9a099012ed7fa21e46165ac12091d86727e80`；实际临时报告 SHA256 为 `887e3a563fc27d7c1ba4487ed6e8c8e5c213433b7b44d31915fa97c4de72ba55`，报告 20,744 bytes。报告数值由此命令重生，不提交原件。

此前宽的全图 metric 角位移估计只得到 $|C|<1.49\cdot10^{-6}$、二阶组合小于 $.009602$；本结果用实际中央 $D$ 的严格累计积分把它收紧到第 4 节的值。旧宽计算没有用来冒充新界。独立非零控制系数与 SciPy 的导数接口比较中，零、一、二阶最大差分别为 $0,4.07\cdot10^{-20},4.34\cdot10^{-19}$；这个数值接口检查不替代 (14) 的连续证明。

本结果保存准确归一参考的全时几何及可消费的全半体连续 jet 入口。完整新 field 仍须自己的连续几何消费、全域残差及同 $g$ 加密记录；强幅度目标也没有由此解决。
