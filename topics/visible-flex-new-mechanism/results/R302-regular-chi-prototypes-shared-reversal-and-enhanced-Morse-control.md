# R302：新 χ 原型的整字正则化、真实共享倒行与增强 Morse 控制

日期：2026-11-15。**完整纸面存在证明；没有运行新的科学、符号、profile、开发或几何计算。**

本稿接 [R297 九个真实平台矩观测](R297-ordered-platform-matrix-surjective-pure-zero-responses-and-real-control.md) 和 [R298 单个真实 self 观测](R298-zero-platform-matrix-with-nonzero-self-response-and-ten-observation-control.md)，补齐它们当时明确保留的几何正则性接口。新增的 $\chi_{30},\chi_{32},\chi_{37},\chi_{40}$ 不是由第三对角覆盖可以替换掉的完整算子。本稿不要求这些算子在自由几何扰动中逐个保持不变；准确保持低阶条件的是包含它们的**完整 R101 共享路径字**。

先在基点建立含全部真实成本的增强截面；随后允许第三原型漂移，再用完整增强 IFT 恢复全部目标。这样可同时保持全 pure、平台矩阵以及一个固定非零 profile 的 self 值，并安装共同例外偶端芽、选取全域 Morse 的 $h$。完整 canonical period、逐 ruling、全部 self 函数或其他未纳入的观测不由此归零。

主要来源：[R70](R70-zero-matrix-bridges-and-affine-complete-fourth-period.md)、[R71](R71-third-holonomy-commutators-and-complete-fourth-P1.md)、[R77](R77-weight-three-local-operator-actual-finite-controllability.md)、[R83](R83-true-fourth-transfer-and-zero-lower-history-variations.md)、[R101](R101-finite-replication-and-signed-fourth-character-costs.md)、[R214](R214-nowhere-constant-closed-hook-with-exact-universal-pure-zero.md)、[R222](R222-simultaneous-real-pure-and-eight-flux-control.md)、[R223](R223-Morse-closed-hooks-with-exact-pure-and-eight-flux-constraints.md)、[R225](R225-complete-period-range-flat-end-germs-and-finite-observation-quotient.md)、[R227](R227-realizable-quadratic-k-even-ports-and-the-exceptional-germ.md)、[R241](R241-complete-sigma-four-layer-and-resonant-exceptional-germs.md) 及 [R254](R254-eight-exact-third-diagonal-lifts-and-eighteen-dimensional-image.md)。

## 1. 结论与固定对象

区分第三传递算子 $T_B$ 和 R297 的有序平台矩阵 $\mathcal T(V_B)$。仍用原有限真实成本空间 $U$、响应空间 $\mathcal R$，记
$$
\mathcal P=\pi U,\qquad \mathcal L=\pi\mathcal R,\qquad
\mathcal Q=\mathcal P/\mathcal L.
\tag{1}
$$
不假设 $\mathcal Q=0$。

共同物理区间 $I$、右锚、固定查询及 profiles 遵守第 11 节的选择顺序。取一个固定非零实函数 $u_*\in C_c^\infty(I)$，定义全 $U$ 上的线性观测
$$
F_9(V)=\mathcal T(V)\in\operatorname{Mat}_3(\mathbb R),
\qquad
F_{10}(V)=\bigl(\mathcal T(V),q_{u_*}(V)\bigr),
\tag{2}
$$
其中
$$
q_{u_*}(V)=\frac14[x^2]_{\rm left}V(u_*^2,0).
\tag{3}
$$
式 (2) 沿 R297/298 的原查询延拓定义，不先要求目标满足 pure 零或平台零。令
$$
E_m=(\pi,F_m):U\longrightarrow
\mathscr E_m=\mathcal P\oplus\mathbb R^m,\qquad m=9\ \text{或}\ 10.
\tag{4}
$$

**定理 A。** 可以从一开始选定有限真实原语库、共同合法 $I$ 和 (2) 的查询，使对任意指定目标 $y_*\in\mathscr E_m$，存在有限光滑同端口路径 $D$ 满足
$$
M_D=T_D=0,\qquad F_{\rm end}=F_{\rm start},\qquad
E_m(V_D)=y_*.
\tag{5}
$$
它可同时满足以下性质：

1. 全部外部共享端口采用第 7 节准确的解析偶 germ；原语内部的有限拼口也被纳入该节的安装或自由扰动范围，没有冻结的常段后缀。
2. 在选定的非零端曲率参数 $\varkappa$ 上可取 $\epsilon=\varkappa^2/4>0$；这是同一个二维参数开邻域内的选择。
3. 整条实际路径满足
   $$
   h_s=0\ \Longrightarrow\ h_{ss}\ne0.
   \tag{6}
   $$
4. 在该指定目标的一个邻域内有相同有限字、整数、germ 和自由参数所给的 $C^1$ 真实目标截面；邻近成员仍满足 (5)、(6)。

**定理 B。** 对固定非零第三 hook 强度 $\kappa_{\rm h}$，可取真实有限闭 hook $X$，使
$$
\begin{gathered}
M_X=0,\qquad T_X=\kappa_{\rm h}\mathfrak H,\qquad
F_{\rm end}=F_{\rm start},\qquad
\alpha_{\rm end}=\alpha_{\rm start},\\
\pi V_X=0,\qquad \mathcal T(V_X)=A,\qquad
q_{u_*}(V_X)=b
\end{gathered}
\tag{7}
$$
对任意给定 $A\in\operatorname{Mat}_3(\mathbb R)$、$b\in\mathbb R$ 准确成立，并同时具有上述端芽和全域 Morse 性。$\kappa_{\rm h}$ 与端曲率参数 $\varkappa$ 是两个不同量。

这里只控制一个预先固定的 $u_*$。没有把 (7) 解释成 $q_u=0$ 对所有 $u$，也不声称能在任意已冻结的窄 $I$、固定总长或原固定度量中改造一条任意旧几何。

## 2. 四个 χ 的完整真实来源

R254 的原模板来源表给
$$
\begin{array}{c|c|c}
j&\tau_j\text{ 的原来源}&\text{状态单项}\\ \hline
30&\text{R77 area}&h^{-5}k\\
32&\text{R77 area}&h^{-4}\\
37&\text{R77 area}&h^{-3}k\\
40&\text{R77 area}&h^{-2}
\end{array}
\tag{8}
$$
R77 §5 证明这些完整 Laurent 系数属于真实第三可达空间；§6 用有限实际 loops、固定有限重复和完整矩阵零拼接实现每个指定算子。其对有界参数族的真实实现可以固定有限字并光滑选择。这里没有把形式列非零或对角非零当成可达性证明。

沿 R254 的完整交换子索引，
$$
\begin{aligned}
\gamma_{30}&=(3C_2+C_{20})/256,\\
\gamma_{32}&=(C_3-3C_4-C_8)/128-C_{21}/512,\\
\gamma_{37}&=(C_5+C_9+2C_{10})/32,\\
\gamma_{40}&=-C_{11}/32,\\
\chi_j&=\tau_j-\gamma_j.
\end{aligned}
\tag{9}
$$
每个 $\gamma_j$ 是完整三槽 R71 交换子的有限组合。R71 用真实正负参数和有限拼接实现 $-\gamma_j$；它不是负成本。将其与实现 $\tau_j$ 的 M0 路径相接，得到实际有限原型
$$
M_{L_j}=0,\qquad T_{L_j}=\chi_j,\qquad
F_{L_j,\rm end}=F_{L_j,\rm start}.
\tag{10}
$$
同一右锚、完整第二/第三传入历史及第四基准 $v_j=V_{L_j}$ 全部保留。

R254 的 $\Delta\chi_j=0$ 只用于 R297/298 的 pure-zero 响应事实；不用于把 (10) 的完整第三算子置零，更不用于把它换成一个具有相同 diagonal 的 R71 原型。

若要在共同端状态 $S_\theta$ 与原型原端口之间搬移，取 R70 的 M0/frameI 桥 $C_\theta$，使用
$$
L_{j,\theta}^{\,0}=C_\theta L_j C_\theta^R.
\tag{11}
$$
零矩块的第三加法和真实倒行给 $T_{L_{j,\theta}^{\,0}}=\chi_j$，而第四基准为 $v_j+2V_{C_\theta}$。在一个固定小端数据邻域中，$C_\theta$ 的有限辅助整数与字都可固定；(11) 是光滑真实族。搬移不需要省掉连接成本。

## 3. 保留基点 χ 的正则前缀

仅在 $L_j$ 前加一个任意正则 M0 桥，会把其第三原型改成 $\chi_j+T_A$；这不足以直接继承 R297/298 的原响应矩阵。为保留正确基点，采用成对前缀。

取 R70 正则族 $A(a,F,\theta)$，其中 $a\in\mathbb R^8$ 是内部矩阵参数，$F\in SO(3)$ 是指定末 frame，$\theta$ 收集端口和其他固定小族参数。在基点可平移 $a$ 坐标，使
$$
M_{A(0,I,\theta)}=0,\qquad
D_aM_A\ \text{可逆}.
\tag{12}
$$
对所有邻近 $a$，frame 与 omega 终值按指定端数据准确满足。记 $A_0(\theta)=A(0,I,\theta)$，定义
$$
\widehat L_j(a,F,\theta)
=A(a,F,\theta)\,A_0(\theta)^R\,L_{j,\theta}^{\,0}.
\tag{13}
$$
后两块按前一块的真实 frame 作同一 ambient 放置，因其相对末 frame 为 I，整字末 frame 是 F。在 $a=0,F=I$，
$$
M_{\widehat L_j}=0,\qquad
T_{\widehat L_j}=\chi_j,\qquad
V_{\widehat L_j}=2V_{A_0}+V_{L_{j,\theta}^{\,0}}.
\tag{14}
$$
此外 $D_aM_{\widehat L_j}=D_aM_A$ 仍可逆。R70 内部正负辅助圆及其连接保证 $k_s\not\equiv0$；这不依赖外端 $k_e$ 非零。

现在把**整个 (13)** 视为 R214 §3.3 的一个正则实际原语，而不是只允许前缀变化。用固定归一化坐标保存真实长度，在全部内部加入自由光滑 $h$ 扰动 $\eta$，另取紧支撑 $\zeta$ 使
$$
c_\omega=-\frac12\int\frac{k_s\zeta}{h^2}\,ds\ne0.
\tag{15}
$$
在相应坐标中令
$$
\widehat h=h_{a,F,\theta}+\eta+b\zeta,\qquad
\widehat k=k_{a,F,\theta},\qquad
\widehat\omega(s)=\omega_-+\int_{s_-}^s
\frac{\widehat k_s}{2\widehat h}\,d\tau.
\tag{16}
$$
原语的完整矩阵和 omega 末值由九个方程恢复：
$$
G=(\widehat M,\widehat\omega(s_+)-\omega_+)=0,\qquad
D_{(a,b)}G=
\begin{pmatrix}D_aM&D_bM\\0&c_\omega\end{pmatrix}.
\tag{17}
$$
在足够高的有限 $C^r$ 参数空间上此块可逆；先用有限参数 IFT，随后限制到光滑 $\eta$。

自由扰动允许遍及原 $L_j$、搬移桥、旧固定后缀及其内部平段。扰动后不要求 (13) 中原来的 $A_0^R$ 子串仍是当前 $A(a)$ 的逆，不要求原子串各自 M0，也不要求
$$
T_{\widehat L_{j,\eta}}=\chi_j.
\tag{18}
$$
准确保留的是整块 M0、真实端口和 frame。其实际第三算子记为 $\tau_j(\eta)$；在基点 $\tau_j(0)=\chi_j$。后文使用的是**整个已修正长块的真倒行**，不是那个已失去子逆意义的旧子串。

这一步既保住已知响应矩阵的正确基点，又为所有隐藏后缀提供自由 $h$，没有以冻结一段旧路径换取可逆性。

## 4. 第三原型漂移不破坏 R101 的完整低阶恒等式

以下是所需的整字事实。固定任意当前参数 $\eta$，设实际路径 $L_\eta$ 满足
$$
M_{L_\eta}=0,\qquad T_{L_\eta}=\tau_\eta,\qquad
V_{L_\eta}=v_\eta.
$$
$\tau_\eta$ 不必属于固定的一条线，也不必仍对角为零。取实际二阶族 $A_\eta(t)$，保
$$
\Phi_{M_{A_\eta(t)}}=tE.
$$
所有正负参数、重复出现和倒行共用同一个修正族。定义
$$
\begin{aligned}
C_\eta(t)&=A_\eta(t)A_\eta(-t),\\
W_\eta(t,n)&=A_\eta(t)L_\eta^n
 A_\eta(-t)(L_\eta^n)^R,\\
Z_\eta(t,n)&=W_\eta(t,n)C_\eta(-t)^R.
\end{aligned}
\tag{19}
$$
$n$ 始终是一个固定有限正整数。

原 R83/R101 的完整传递为
$$
A_{12}=A_1+A_2,\qquad
T_{12}=T_1+T_2-A_2(\,\cdot\,,A_1D).
\tag{20}
$$
对 M0 块，
$$
T_{B^R}=-T_B,\qquad V_{B^R}=V_B,
\tag{21}
$$
且拼接的第三、第四成本各自相加。令
$$
H_\eta(t)=T_{A_\eta(t)}+T_{A_\eta(-t)}
+t^2E\circ E=H_\eta(-t).
$$
把 (20) 逐段用于 (19)，$n\tau_\eta$ 与其实际倒行的 $-n\tau_\eta$ 准确相消，得到
$$
M_C=M_W=0,\qquad T_C=T_W=H_\eta(t),
$$
因而
$$
\boxed{M_{Z_\eta(t,n)}=T_{Z_\eta(t,n)}=0}
\tag{22}
$$
对每个允许 $\eta$ 是完整函数身份。证明没有用到 $D_\eta\tau_\eta=0$。

同一完整第四传递还给
$$
\boxed{
V_{Z_\eta(t,n)}
=E_0(t,\eta)+n\{2v_\eta+t\mathcal B_E(\tau_\eta)\},
}
\tag{23}
$$
其中
$$
E_0(t,\eta)=V_{C_\eta(t)}+V_{C_\eta(-t)}
$$
是实际偶基准，$\mathcal B$ 为原完整响应。每个固定参数处，式 (23) 的基准与 n 无关。扰动后 $v_\eta$ 和响应的 pure 部分均可变化；本文不把它们置零，也不把 $\mathcal B_E(\tau_\eta)$ 继续标成原来的 $\mathcal B_E(\chi_j)$。

相同原语出现之间的共享是必要条件。如果把 $L_\eta^n$ 与其后所谓“逆块”独立改变为无关路径，或在正负 t 处采用不相干的修正，(22) 不再由上述证明成立。整块真倒行必须由当次实际 $h,k,\omega$、frame 和时长产生。第四倒行仍是正号，不提供形式负路径。

## 5. 在新基准上先建立完整增强截面

R297 给九个实际响应
$$
R_{ij}=16\mathcal B_{\Phi_{p_j}}(\sigma_i),\qquad
(\sigma_0,\sigma_1,\sigma_2)
=(64\chi_{32},-32\chi_{37},64\chi_{40}),
\tag{24}
$$
其 pure 为零且 $\mathcal T(R_{ij})$ 为九个矩阵单位。

R298 另给
$$
K_*=\mathcal B_{\Phi_{r_0}}(\chi_{30}),\qquad
\pi K_*=0,\qquad \mathcal T(K_*)=0,
$$
$$
q_{u_*}(K_*)=
\frac3{512}\int (u_*'')^2(u_*''')^2>0.
\tag{25}
$$
通过 R298 的三角列修正，得到 $m=10$ 个 pure-zero 响应，使 $F_{10}$ 矩阵可逆。记一般所选有限组为 $K_1,\ldots,K_m$；其完整第三原型按第 2–3 节正则化。

正则前缀和端口搬移改变第四基准。必须**在这些新基准上重新执行 R222**，而不是沿用旧数值或旧目标参数。对每组原响应，先记全部真实基准和 $v_j$，用 R214 的正则 full-pure 截面追加一个 M=T0 块，使该组基点的总基准 $\widehat v_j$ 满足
$$
\pi\widehat v_j=0.
\tag{26}
$$
它的 mixed 成本仍保留。追加的校正块也纳入有限正则库；若将它并入一个第三原型作为固定后缀，整块正则导数仍由 (12) 给出，后续自由扰动遍及这个后缀。

在 $\eta=0$，R101 和有限组合给
$$
V_Z=E_0(t)+n\left(2\sum_j\widehat v_j+
\sum_jt_jK_j\right).
\tag{27}
$$
R222 先用完整 pure 截面校正 $p-\pi E_0(t)$，保留该校正的全部 $F_m$ 成本；再用一个有限大 n 同时支配基准值界和导数界，得到严格收缩的不动点。原纯商 $\mathcal Q$ 始终保留，不能只校正最后 m 个坐标。

由该已付构造，在目标 $y_*$ 附近得到固定有限字
$$
\mathscr D_0(v),\qquad
E_m(V_{\mathscr D_0(v)})=v,\qquad
D_vE_m(V_{\mathscr D_0(v)})=I_{\mathscr E_m}.
\tag{28}
$$
全部辅助整数、重复次数、原语索引和其正反向在这个邻域固定。

原 full-pure 模块使用 R214 已正则化的满锥见证与 R71 交换子结构。新增 χ 模块则用 (22)。两者的低阶保持理由不同，但组合后的实际字仍 M=T0。没有用 R208 的 diagonal 覆盖替代新 mixed 原型。

此后对全库加入共享自由参数。式 (26)、(27) 中分别为零的中间量不必继续为零；基准、pure 校正、漂移响应及其全部传递变化都进入最终真实成本。固定 n 很大只会要求更小的后续参数邻域，不产生一个尚未取到的无限复制极限。

## 6. 新成本仍在原 U；用完整目标方程恢复漂移

相同平端口的 M0 块仍属于原 U；安装第 7 节端芽后也一样。准确理由是 R109/R129/R130 的原式，而不是为新路径重新定义空间。

有关端势分别是速度线性、速度乘加速度和速度三次；$N_2$ 为速度二次。在外端
$$
h_s=k_s=0
\tag{29}
$$
已使这些势和 $N_2$ 全为零。$N_0$ 本身不设为零，其初势项由整体 M0 消去。原 R130 系数呈示和响应项仍给
$$
V_B\in U
\tag{30}
$$
即使 $T_B\ne0$。也可以用真实 $BB^R$ 的 M=T0 和成本 $2V_B$ 检查线性空间归属，但不能把这一半倍解释成实际分数次路径。

对足够高的有限 $C^r$ 参数邻域，R56 全场恢复、完整 ODE 历史和成本对参数为 $C^1$；光滑逼近及 U 的有限维闭性给所用 Banach 邻域的同一归属。共同正分母和 h 下界另在第 11 节保持。

令 $\theta$ 暂包括端数据和端芽参数，写全部修改后的实际字为 $\mathscr D_{\eta,\theta}(v)$。由 (22) 和旧 pure 模块的结构，整字仍 M=T0。定义
$$
\Phi(\eta,\theta,v)=E_m(V_{\mathscr D_{\eta,\theta}(v)})
\in\mathscr E_m.
\tag{31}
$$
在原基点 $\theta=\theta_0$，
$$
D_v\Phi(0,\theta_0,v_*)=I_{\mathscr E_m}.
$$
因此完整目标 IFT 给
$$
v=v(\eta,\theta,y),\qquad
\boxed{\Phi(\eta,\theta,v(\eta,\theta,y))=y.}
\tag{32}
$$
所有中间成本变化已经包含在 (31)，包括 $nD_\eta v_\eta$、$ntD_\eta\mathcal B_E(\tau_\eta)$、原纯校正的变化及各偶基准。式 (32) 不需要单独求解第三原型的全部三槽保持方程。

这正补足 R225 §10.3 的实现缺口。那里的警告没有错误：响应满秩或 R96 的有限查询并不提供“任意原型 T 逐个固定”的自由族。本稿证明的是另一项充分结构：整字 (22) 对任意漂移的 $\tau_\eta$ 仍成立，加上基点的完整增强截面 (28)，便足够做 (32)。若某个未来完整 period 商已满足 R225 的响应满秩前提，此方法可应用于其有限实际 R101 生成库；本稿没有替它证明那项尚未给出的满秩前提。

## 7. 从同一二维邻域安装共振例外偶 germ

将外共同端状态作为真实外参数，规定
$$
S_{\varkappa}=(h_e,\varkappa,\varkappa/h_e),\qquad h_e>0.
$$
在 $(\varkappa,\epsilon)=(0,0)$ 一次选定第 2–5 节的有限库、端口搬移桥及所有整数。R70 对端数据的小邻域有同一固定有限辅助整数和光滑依赖；内部矩阵正则性及 (15) 来自内部辅助圆与连接，不要求外端 $\varkappa\ne0$。

在每个指定共同外端的真实物理距离 $\sigma$ 中，安装
$$
\boxed{
h=h_e e^{\epsilon\sigma^2},\qquad
k=\varkappa(1-2\epsilon\sigma^2),\qquad
\omega=\frac{\varkappa}{h_e}e^{-\epsilon\sigma^2}.
}
\tag{33}
$$
水平方程 $\omega_s=k_s/(2h)$ 准确成立。三式在 $(0,0)$ 联合光滑，没有 $1/\varkappa$ 或 $1/\epsilon$。

### 7.1 先三维 frame，再九个原约束

按照 R227，在原常 collar 内用物理 $\sigma=s-s_e(a,F,\theta)$ 和固定核心 cutoff 预修改 h、k。因为 k 变化，不能沿用“h 扰动不改 frame”来省掉 frame 修正。以指定末 frame F 为外参数，预修改后的末 frame 映射在 $\epsilon=0$ 恰为 F，故其 F 导块为 $I_3$。先解三维 frame 方程，得到 $F=\widehat F(a,\varkappa,\epsilon,\theta)$。

再加入只改变 h 的 masked 自由 $\eta$ 和 $b\zeta$，从真实首 omega 积分。消 frame 块后，九约束在联合基点仍为
$$
D_{(a,b)}G=
\begin{pmatrix}D_aM&*\\0&c_\omega\end{pmatrix},
\qquad \det D_aM\ne0,\quad c_\omega\ne0.
\tag{34}
$$
所以 (32)、frame IFT 与 (34) 共同给含 $(0,0)$ 的真正二维参数开邻域。

在这个开邻域选足够小的 $\varkappa\ne0$，再取
$$
\boxed{\epsilon=\varkappa^2/4>0.}
\tag{35}
$$
不是由每个固定 $\varkappa$ 的某个未知阈值推断 (35) 合法。分析偶部子空间时出现的倒数系数不进入本安装的方程或 Jacobian。

### 7.2 内部拼口、真倒行和端值

各原语内部所有旧拼口列入有限名单。可按 R227 同样安装
$$
h=h_{e'}e^{\epsilon\sigma^2},\quad
k=k_{e'}(1-2\epsilon\sigma^2),\quad
\omega=b_{e'}+k_{e'}/h.
\tag{36}
$$
其中内部 $b_{e'}$ 是整条真实 omega 积分给出的中心常数，可以随参数变化，不被重置为旧值。内部两侧属于同一个真实解，不需要额外伪造一个 omega 端点方程。也可不保护某个内部旧接口而允许自由 h 跨过它；不能留下既不保护又不能扰动的固定平段。

外部相接原语的端值由原约束精确固定；共享的 (33) 全偶，所以真倒行和重复具有函数级、全 jet 匹配。正 H 与 omega 平移按 R227 保留同类 (36)，不要求所有内部不同 $k_{e'}$ 都满足 (35) 的同一共振比例。本文的共振声明准确指从起点共同指定的外端。

在所有保护核心，
$$
h_{ss}=(2\epsilon+4\epsilon^2\sigma^2)h>0.
\tag{37}
$$
式 (29) 在拼口中心成立，所以旧 U 归属和原真实传递继续适用。保护核之外保留任意局部 masked h 扰动，下一节在完整约束下使用它。

## 8. 新九/十观测对自由几何仍给光滑积分密度

为了使用 Morse 论证，不能只凭 $F_m$ 有限维就宣称其几何导数没有点约束。下面支付所需性质。

固定当前精确解和一个原语内部开区间 J，其 closure 避开保护核心。暂冻结有限内部参数，在 J 上取 $v\in C_c^\infty(J)$ 作为 h 扰动。对固定 profiles、右锚和输出点，R56 的完整有限场恢复及其真实 $s$ 历史是一组有限 ODE。线性化并用真实初值的 Duhamel 公式，得到
$$
D_\eta\operatorname{ev}(V)[v]
=\sum_{\ell=0}^{L_*}\int_J A_\ell(s)v^{(\ell)}(s)\,ds,
\qquad A_\ell\in C^\infty(J).
\tag{38}
$$
$L_*$ 有限。式 (38) 包括扰动对其后所有块的传入第二、第三历史和最终周期的影响，不能在下一块首把它们置零。变量时长用固定原语坐标写出，正 Jacobian 及有限导数吸收进 $A_\ell$。

R297 的 $\mathcal T$ 由固定三左、三右 profiles 和有限第四振幅系数查询承载；振幅系数可用固定有限多项式插值提取，左二次尾可用固定三个左输出点提取。R298 的 $q_{u_*}$ 同样为固定 profile 上的左二次尾查询。因此每个新增坐标都是固定有限个这种真实评价的实线性组合。式 (38) 对它们成立；它们在 profile 变量 x 的点值不是几何变量 s 的 Dirac 点约束。

纯空间的有限坐标也沿 R220/R225 的有限真实查询表示处理。于原低阶保持族内，由有限 U 的身份把坐标写成真实查询，再求导，而不是先对一个未经证明存在的极限系数求导。故全部增强坐标、八矩与 omega 约束导数，经紧支撑 s 分部积分均有
$$
\boxed{L_\nu(v)=\int_J b_\nu(s)v(s)\,ds,\qquad
b_\nu\in C^\infty(J).}
\tag{39}
$$
frame 的自由 h 导数在有限参数冻结时为零。内部隐参和 (32) 的导数只作有限可逆矩阵运算，仍是 (39) 的有限组合。

同名原语在多个正反向或缩放出现位置的变化只是有限个拉回的 (38)。它增加有限行，不引入一个可独立变化的假副本。隐藏原接口是实际光滑点；真实历史在此连续，不产生跳跃点源。外端势另外由 (29) 支付，本文不把外端分布项冒称为内部光滑密度。

## 9. 在所有增强目标精确保持时取得全域 Morse

此时固定非零 $\varkappa$、正 $\epsilon$ 和目标 y，使用已经非线性解好的族
$$
\eta\longmapsto
\mathscr D_{\eta,\theta}\bigl(v(\eta,\theta,y)\bigr).
\tag{40}
$$
在一个未保护的源点附近，列出以下有限线性行：

- 同一原语每个真实调用的九约束自由导数为零；
- 在外部 v 暂固定时，整个增强映射 (31) 的自由导数为零。

由 (39)，它们全是光滑积分密度。若这些行共同核上的
$$
v\longmapsto(v'(s_0),v''(s_0))
\tag{41}
$$
不满射，则某个非零 $-a\delta'_{s_0}+b\delta''_{s_0}$ 等于有限个光滑密度的组合，矛盾。正 mask 在小 J 内可除去，不改变此结论。

在这样的方向上，(32) 与 $D_v\Phi$ 可逆先给外部参数变化 $\delta v=0$；九约束可逆再给各调用的内部修正参数变化为零。因此真实时长、缩放、frame 校正、接口位置等一阶不动，实际 h 的变化就是共享源扰动的拉回。

若出现 o 的真实速度为 $\lambda_o=ds/dx>0$，源坐标为 $\sigma_o(x)=x$ 或 $1-x$，正缩放为 $c_o$，则
$$
\delta h_s=\frac{c_o\sigma_o'}{\lambda_o}v',
\qquad
\delta h_{ss}
=\frac{c_o(\sigma_o')^2}{\lambda_o^2}v''
-\frac{c_o\sigma_o'\lambda_o'}{\lambda_o^3}v'.
\tag{42}
$$
关于 $(v',v'')$ 的行列式为 $c_o^2\sigma_o'/\lambda_o^3\ne0$。于是每个未保护实际点的 $(h_s,h_{ss})$ 在精确约束族中都有满射导数。这没有给同一原语的副本虚构独立参数。

保护核心由 (37) 已无坏点。其余有限出现位置的紧区域中，坏点联合集紧；在每个坏点选两条光滑方向，有限覆盖得到 $v_1,\ldots,v_N$。考察 (40) 中的有限参数族 $\eta=\eta^0+\sum t_\nu v_\nu$。缩小参数球后，映射
$$
(t,x)\longmapsto(h_s^o(t,x),h_{ss}^o(t,x))
$$
在全部零点上为 $C^1$ submersion，零集为维数 $N-1$ 的流形。它投影到 N 维参数球的像为零测集：可数紧坐标图给从低一维空间的 Lipschitz 像，有限出现位置的并仍零测。故任意小球中有一个光滑参数 $\eta^*$，消去所有 $h_s=h_{ss}=0$。

这正是 R220/R223 的有限维零集投影论证；不调用未付的无限维 Sard 定理。实际场作为 $C^3$ 函数的参数映射为 $C^1$ 足够，前文已取高阶有限 r。

在选定参数处，整个有限闭合参数区间上
$$
\min\bigl(|h_s|^2+|h_{ss}|^2\bigr)>0.
\tag{43}
$$
固定 $\eta^*$、$\varkappa,\epsilon$，只改变 y，式 (32) 的 $C^1$ 截面及几何的 $C^2$ 连续性保 (43)。所以得到的是一次 Morse 选择之后的真实目标邻域截面，不是对每个目标不连续地重新作泛性选择。

## 10. 闭 hook、全部基准与实际位移

闭 hook 的背景沿 R214/R223 原库选取。它的完整第三算子由 R71/R72 结构字保持为固定 $\kappa_{\rm h}\mathfrak H$；这里不能允许背景 hook 强度无约束漂移。背景中所有正则原语也加入前述自由参数、保护核心及有限出现列表。

将同一个控制块插入 Klein 的一类 prototype，其四个正确 ambient 副本给全增强目标
$$
\Psi(\eta,\theta,v)
=E_m(V_{X^0_{\eta,\theta}})
+4E_m(V_{\mathscr D_{\eta,\theta}(v)}).
\tag{44}
$$
基点对 v 的导数为 $4I_{\mathscr E_m}$。对 (7) 的目标
$$
(0,A,b)\in\mathscr E_{10}
$$
应用完整 IFT；m9 情形删最后坐标。然后第 8–9 节使用 (44) 的全部导数行，背景和控制成本均在精确约束中。没有先选一个 Morse 背景，再漏计后加控制块所带来的平点或成本。

所有插入块 M=T0，原真实传递保背景的完整第三 hook。Klein 闭合始终使用改变后 prototype 的真实位移，四个实际向量按原作用相消。不要求各控制块自身零位移，不重置 $\alpha_s=h^2T$ 的积分，也不在最后另添一条未计成本的闭合路径。末 frame 与 scalar germs 准确匹配。

于是 (44) 同时给 (7)、全域 Morse 与指定偶端芽。负目标通过真实有限 R222 控制取得，不把有符号响应向量直接冒成实际负成本。

一个直接新推论是：可在 $\mathcal T=0$、whole pure 为零、共同共振外端及 Morse 类中，令这个固定 $q_{u_*}$ 取任意指定实值，包括严格正或严格负。这推进 R298 的实际范围；它仍不意味着同一条几何的 $q_u$ 全函数可任意指定，也不等于保持另一冻结几何的同一度量。

## 11. 共同 I、profiles、整数与参数的选择顺序

整个选择可以按以下有限顺序完成。

1. 固定原 full-pure 控制所需的有限库、有限满锥见证、W71 原型及其正则实现；加入四个 χ 的完整实际原型、端口搬移和 (13) 的正则前缀。闭 hook 应用还在此加入背景与全部 scalar/frame 桥。
2. 将共同外端 $\varkappa$ 和指定 frame 作为 R70 的外参数，在 $\varkappa=0$ 的一个紧小邻域选一次有限辅助整数和正则库。固定原型基准，按 R222 先付各组 pure 基准；这只用同一有限小族和以后可增加的固定重复。
3. 由整个有限库的紧 scalar 包络选择共同正支区间 I，保证 $h>0$ 和 $x+\omega>0$ 有严格余量。此后固定右锚、R297 的九个查询及一个非零 $u_*$；(25) 对任何这样的 $u_*$ 都严格非零，故三角满秩无需再扩原几何库。若另外固定合法圆，其选择也在此，随后不移动。
4. 在这个固定观测下重新计算式 (26) 所指的真实基准作为数学对象，按 R222 确定覆盖目标的有限参数盒、full-pure 校正与最后 n；这是存在论证，没有运行新的评价。基点取得 (28)，所有整数和有限词固定。
5. 对全部原语同时作第 7 节安装，并用 (32) 或 (44) 的完整目标 IFT。所有已经固定的正余量在足够小的参数邻域中保持。
6. 在同一二维邻域选 $\varkappa\ne0,\epsilon=\varkappa^2/4$，随后在选定正 $\epsilon$ 的精确约束族中作一次 Morse 选择。没有在 $\varkappa=0$ 声称 Morse，也不需要正 Hessian 下界统一延伸到 $\varkappa=0$。
7. 最后固定这次选择，仅允许目标在其小邻域变化，取得第 9 节的局部截面。

大有限复制增加总长与位移，不扩大已固定的小族 scalar 包络。取定有限字后的扰动阈值可以依赖它；本文不声称对无限复制有统一阈值。若从一个已有严格物理余量的 I 出发且全部新正则库已在其内，亦可直接保持这个 I；否则结论是上述新共同 I 的构造，不是任意狭窄旧区间的改造定理。

## 12. 本稿补齐的实现与仍未支付的层

新结论的实质是三个准确步骤相接：

- 基点用成对正则前缀保住完整 χ，同时计入真实第四基准；
- 扰动中允许第三原型漂移，以共享整个原型及真倒行使完整 R101 字始终 M=T0；
- 用原 U 上的完整增强目标方程恢复全部 pure 与九/十观测，再在其精确解族内取 Morse 与共振偶端芽。

因此 R297/298 的新增 χ 响应不再因为缺少“逐个第三原型固定”的自由族而被挡在 R223 型正则几何之外。这个结论来自真实字的传递恒等，不来自 diagonal 覆盖，也不来自把代数导子当实际非仿射几何变换。

本稿没有证明某个固定圆的全 canonical mixed period 为零，没有解同一个二阶 gauge 的整个 period/ruling 问题，也没有自动保持 R280–R294 在另一预先选定几何上得到的 Gaussian 系数。若要同时加入更多观测，须从起点证明相应真实响应满秩或另给准确控制；不能把有限性代替可达性。

选定最终几何后，才有其同一度量、同一个圆和同右锚目标。几何设计中的变化一般改变度量。嵌入、reach、厚度、宏观幅度、高阶收敛和有限等距族仍不在本稿结论内。
