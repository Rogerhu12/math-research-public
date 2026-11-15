# R163：完整正规系数的八矩 cocycle 与单权字符头部

日期：2026-11-15。**纸面已证明。** 本稿将 R146 的最高层协变延伸到完整五项速度四次式，并对静态、速度二次层给出必须保留的同一个八矩 cocycle。它把完整字符头部所需的平移像写成同一真权正规系数的明确线性组合；不需要另算相邻权的原目标，也不把低阶平移像误写成单独的状态微分。

依据 [R73](R73-pointwise-eight-matrix-and-local-third-bridge.md)、[R89](R89-affine-covariance-and-positive-multiple-pair-P1.md)、[R105](R105-finite-canonical-fourth-cost-space-and-response-quotient.md)、[R109](R109-local-density-of-the-complete-fourth-quotient.md)、[R127](R127-positive-affine-character-of-the-fourth-cost-cone.md)、[R129](R129-horizontal-geometry-IBP-for-complete-fourth-costs.md)、[R130](R130-true-fourth-span-from-horizontal-normal-coefficients.md)、[R140](R140-full-action-multiplier-equivalence-for-real-cost-positivity.md)、[R145](R145-true-curvature-reflection-and-even-positive-characters.md)、[R146](R146-acceleration-family-quotient-covariance-and-eighty-seeds.md) 和 [R159](R159-balanced-mixed-faithfulness-after-pure-cancellation.md)。

没有进行新的研究符号计算、profile 评价、响应编译或几何路径计算。特别地，本稿不预报字符头部维数，不宣称正字符不存在，也不宣称完整第四 period 已获实际支付。

## 1. 同一八矩规范化及十四族

记真实完整第四空间与响应空间为

$$
U=\mathcal U_4,\qquad R=\mathcal R_8,\qquad Q=U/R.
\tag{1}
$$

继续使用同一 canonical 目标、共同右 collar、完整两个相位模式和全部真实历史。R109 的局部密度及矩阵密度为

$$
L=L_0+L_2+L_4=v-\mathcal B_mN,\qquad m=m_0+m_2.
\tag{2}
$$

这里下标是几何导数权；第三局部势 N 不能与下文的平移生成元混淆。为区分两者，本稿把平移生成元写作 $\mathsf N$。

采用 R130 原来的八个参考状态，顺序固定为

$$
S_i^*=(1,k,d+k),\qquad d\in(0,1,-1,2),\quad k\in(0,1).
\tag{3}
$$

令 $a_i$ 是基 $m_0(S_i^*)$ 的线性坐标，故

$$
M=\sum_{i=1}^8a_i(M)m_0(S_i^*).
$$

设

$$
\Gamma(M)=\sum_i a_i(M)L_0(S_i^*),
$$

$$
F_0(S)=L_0(S)-\Gamma(m_0(S)),\qquad
\widetilde L_2=L_2-\Gamma(m_2).
\tag{4}
$$

由参考坐标的 Kronecker 身份，有原式恒等

$$
\boxed{F_0(S_i^*)=0\quad(1\le i\le8).}
\tag{5}
$$

式 (5) 只在这八个参考状态上成立；没有令一般状态的静态成本为零。式 (4) 对真实的全部矩阵 $m_0+m_2$ 使用同一个 $\Gamma$。

取真实水平变量

$$
S=(h,k,\omega),\quad h>0,\quad
u=h_s,\ w=k_s,\ a=h_{ss},\ b=k_{ss},\qquad
\omega_s=\frac{w}{2h}.
$$

按 R129 的真实

$$
X=\partial_h,\qquad
Y=\partial_k+\frac1{2h}\partial_\omega
$$

作完整分部积分，得到

$$
\widetilde L_2=D_sP_1+\widehat Q_2,\qquad
\widehat Q_2(S;u,w)=\sum_{i=0}^2F_{2,i}(S)u^iw^{2-i},
\tag{6}
$$

$$
\begin{aligned}
L_4={}&D_sP_3+
\bar A_{hh}a^2+\bar A_{hk}ab+\bar A_{kk}b^2\\
&+(H_1u+H_2w)(ub-wa)
+\sum_{i=0}^4F_{4,i}(S)u^iw^{4-i}.
\end{aligned}
\tag{7}
$$

全部 Laurent/log 链式导数、$\mathcal B_{m_0}N^{[2]}$、
$\mathcal B_{m_2}N^{[0]}$、$\mathcal B_{m_2}N^{[2]}$ 和
$\Gamma(m_2)$ 都保留。$P_1,P_3$ 在两端常值 germs 上分别为零，即使两端状态不同也成立。

R130 证明十四个函数族

$$
\mathscr F=
\{F_0;\ F_{2,0},F_{2,1},F_{2,2};\
\bar A_{hh},\bar A_{hk},\bar A_{kk},H_1,H_2;\
F_{4,0},\ldots,F_{4,4}\}
\tag{8}
$$

的每个状态值属于 U，并且

$$
U=R+\operatorname{span}\{F(S):F\in\mathscr F,\ S\}.
\tag{9}
$$

它们的有限 Laurent/log 状态系数具有相同的 span。十四是函数族数，不是维数。

## 2. 仿射作用与八矩修正的准确方向

记 $g=(H,d)$，$H>0$，并令

$$
gS=(Hh,k,(\omega+d)/H),\qquad
(u,w,a,b)\longmapsto(Hu,w,Ha,b).
\tag{10}
$$

R89 的真实作用同时输运 profile、同一个右锚、完整历史和空间相似变换；其在 U、R、Q 上的作用记作 $\mathsf P_g$。所有下述等式均在 Q 中成立。

定义一个从八矩空间到 Q 的线性映射

$$
\boxed{
\mathcal C_g(M)=\sum_i a_i(M)[F_0(gS_i^*)].
}
\tag{11}
$$

方括号表示模 R 的类。式 (11) 的矩阵自变量是原路径的 M，不是变换后的矩阵；状态参数 g 已经作用在参考值上。由 (5)，$\mathcal C_{\mathrm{id}}=0$。

**定理 1（完整正规式的协变与修正）。** 对任意真实状态 S，

$$
\boxed{
[F_0(gS)]=\mathsf P_g[F_0(S)]+\mathcal C_g(m_0(S)),
}
\tag{12}
$$

$$
\boxed{
[\widehat Q_2(gS;Hu,w)]
=\mathsf P_g[\widehat Q_2(S;u,w)]
+\mathcal C_g(m_2(S;u,w)).
}
\tag{13}
$$

对最高层的十个函数族，有没有八矩修正的完整商协变：

$$
\boxed{H^{e_F}[F(gS)]=\mathsf P_g[F(S)].}
\tag{14}
$$

其中

| 族 F | $\bar A_{hh}$ | $\bar A_{hk}$ | $\bar A_{kk}$ | $H_1$ | $H_2$ | $F_{4,i}$ |
|---|---:|---:|---:|---:|---:|---:|
| $e_F$ | 2 | 1 | 0 | 2 | 1 | i |

因此完整 $\widehat Q_4$ 确实享有最高层协变，但低阶两式一般不能删除 $\mathcal C_g$。没有把十四族全部宣布为未经修正的协变函数。

## 3. 端点纤维先给同一个乘子

置

$$
\mathscr L=F_0+\widetilde L_2+L_4=L-\Gamma(m).
$$

固定 g，取任意 $\lambda\in Q^*$，并将它线性延拓到包含所有局部系数及其这一次仿射像的有限真实环境 E，记为 $\ell$。考虑

$$
J_{g,\ell}(B)=
\int_B\ell\{\mathscr L(gS;Hu,w,Ha,b,\ldots)
-\mathsf P_g\mathscr L(S;u,w,a,b,\ldots)\}\,ds.
\tag{15}
$$

它是局部积分，对平端拼接可加，对固定环境旋转不变，并在同 k 真倒行下同号。最后一点使用真实几何导数权仅为 0、2、4；没有把非零矩阵下的完整 V 当作可加量。

若 B 为同 scalar germ、frame $I\to I$、$M_B=0$ 的实际路径，则变换后的路径仍有零 M 和相同 frame 端点。由 R109，

$$
\int_B\mathscr L\equiv V_B\pmod R;
$$

因为 $\Gamma$ 线性，$\int\Gamma(m)=\Gamma(M_B)=0$。变换后同理，R89 的完整 $V_{gB}=\mathsf P_gV_B$ 因而给

$$
J_{g,\ell}(B)=0.
\tag{16}
$$

第三算子无需为零；R105 已将这些零 M 闭端口成本纳入 U。

按 R130 的真实端点纤维论证，对同 germ、同末 frame 和同矩阵的两条路径接上同一条真实补偿路径，可由 (16) 比较它们的 J 值。R70 给任意有限矩阵及 frame 目标和局部光滑截面，因此所得端点函数是
$SO(3)\times E_8$ 上的连续加法同态。SO(3) 的紧性消掉其分量，只剩矩阵线性函数。

随后把任意开 scalar 路径与其同 k 真倒行连接。末 frame 一般为 $ADA^TD$，而不是 I；此时全部 frame 已被前一步处理，矩阵与局部 J 又都是倒行同号，故可以除以二。再用真实零 M 开桥比较 germs，得到一个对全部起止 germs 相同的乘子

$$
\beta_{g,\ell}\in E_8^*
$$

使

$$
\boxed{J_{g,\ell}(B)=\beta_{g,\ell}(M_B)}
\tag{17}
$$

对所有真实开平端 B 成立。这一过程只使用正长度实际路径来比较积分，没有构造第四成本的实际逆元。

现在才允许任意真实时长缩放。固定 scalar 轨迹，取 $s=\delta t$，由 R112 比较

$$
\delta J_0+\delta^{-1}J_2+\delta^{-3}J_4
=\beta_{g,\ell}(\delta M_0+\delta^{-1}M_2)
\quad(\delta>0),
$$

得到

$$
J_0=\beta_{g,\ell}(M_0),\qquad
J_2=\beta_{g,\ell}(M_2),\qquad J_4=0.
\tag{18}
$$

时长缩放一般改变 frame、M；(17) 已经允许这些变化，所以 (18) 没有越出适用路径类。

在任意状态 S 取正长度常路径，第一式给

$$
\ell(F_0(gS)-\mathsf P_gF_0(S))
=\beta_{g,\ell}(m_0(S)).
\tag{19}
$$

代入八个参考状态并使用原式 (5)，得

$$
\boxed{\beta_{g,\ell}(M)=\lambda(\mathcal C_g(M)).}
\tag{20}
$$

这里 $\mathcal C_g(M)\in Q$；右侧只依赖原来的 λ，不依赖延拓如何作用于 U 之外。式 (19)–(20) 对任意 λ 成立，有限维对偶分离即证明 (12)。它也确定 (11) 中必须放原矩阵自变量的方向。

## 4. 二次层的边界与最高四次层的最后一步

对 (18) 的第二式使用 (6)。变换前后 $P_1$ 都在两端常值 germs 上为零；$\mathsf P_g$ 只作用于 profile 系数，与真实 s 微分交换。因此

$$
\int_B\lambda\{
[\widehat Q_2(gS;Hu,w)]-\mathsf P_g[\widehat Q_2(S;u,w)]
-\mathcal C_g(m_2(S;u,w))\}\,ds=0.
\tag{21}
$$

大括号是速度二次式。固定任意状态 $S_*$，令

$$
u_\varepsilon=\varepsilon U,\quad
w_\varepsilon=\varepsilon W,\quad
h_\varepsilon=h_*+\varepsilon\int U,\quad
k_\varepsilon=k_*+\varepsilon\int W,
$$

$$
\omega_\varepsilon=\omega_*+
\int\frac{\varepsilon W}{2h_\varepsilon},
\tag{22}
$$

其中 U、W 是光滑紧支撑速度，$\varepsilon$ 充分小时 $h_\varepsilon>0$。两端为真实常值 germs，但不要求末状态等于初态；(21) 已允许这样的开路径。

将 (21) 除以 $\varepsilon^2$ 后取极限，再取
$(U,W)=(\alpha\psi,\beta\psi)$，得到任意 $\alpha,\beta$ 下的二元二次多项式恒零。故三个系数逐态为零。任意 λ 的分离给 (13)。尤其 $\Gamma(m_2)$ 没有被遗漏。

对 (18) 的最高式，同样用 (7) 消去零端势 $P_3$，得到完整正规式差的零积分。按 R130/R146，先在 (22) 上除 $\varepsilon^2$，分离全部加速度二次系数；然后在它们逐态恒零后除 $\varepsilon^3$，以 $(U,W)=(\psi,\psi')$ 及其交换分离两个面积系数。这里 $\psi$ 可取非负、非零、偶的紧支撑函数，准确的关键积分为

$$
\int\psi\{\psi\psi''-(\psi')^2\}
=-3\int\psi(\psi')^2\ne0,
$$

而另一个面积积分因奇偶性为零。这给 R146 的五个协变式；它们在所有状态恒零，所以其状态变化不会污染下一阶。

余下只有

$$
\sum_{i=0}^4
\lambda\{H^i[F_{4,i}(gS)]-\mathsf P_g[F_{4,i}(S)]\}
u^iw^{4-i}.
$$

再除 $\varepsilon^4$，取同向速度
$(U,W)=(\alpha\psi,\beta\psi)$。因为 $\int\psi^4>0$，关于
$\alpha,\beta$ 的二元四次多项式恒零，五个系数分别为零。所有 $F_{4,i}(S)$ 属于 U，故任意 λ 的分离给 (14) 的五个新四次速度协变式。

这个论证使用的是**零积分**的系数唯一性，不把非负积分读成逐项非负。它依赖完整的 $\widehat Q_4$，不能只对 $v_4$ 作结论，也不能删去其中 $\mathcal B_{m_2}N^{[2]}$。

## 5. 群次序及 cocycle 形式

为固定约定，若先用 $g'=(H',d')$ 再用 $g=(H,d)$，真实状态复合是

$$
g\circ g'=(HH',\,d'+H'd),
\tag{23}
$$

且 $\mathsf P_g\mathsf P_{g'}=\mathsf P_{g\circ g'}$。这不是另一种未说明的标准仿射乘法约定。

令 $\rho_g$ 为 R89 真实二阶算子共轭在 E8 上的线性作用，因而

$$
M_{gB}=\rho_gM_B.
$$

这里只需整个平端路径的矩阵变换，不额外假设某个局部矩阵代表在变换时没有总导数。

由 (6)–(9)，对任意平端 B，$\int_B\mathscr L$ 属于 U：它等于十四族正规系数的积分，全部显式正权边界势为零。记其 Q 类为 $\mathcal I(B)$。式 (17)–(20) 给

$$
\mathcal I(gB)-\mathsf P_g\mathcal I(B)=\mathcal C_g(M_B).
\tag{24}
$$

按 (23) 连续使用两次 (24)，并用 R70 的任意矩阵可达性，得到

$$
\boxed{
\mathcal C_{g\circ g'}
=\mathcal C_g\circ\rho_{g'}
+\mathsf P_g\circ\mathcal C_{g'}.
}
\tag{25}
$$

这明确说明两层必须使用同一个矩阵 cocycle。后面的字符头部结论只需 (12)–(14) 的平移微分，不需要求出 $\rho_g$ 的数值矩阵。

## 6. 平移微分：低阶不是单独的 omega 导数

按已有约定

$$
\mathsf P_{1,d}=\exp(d\mathsf N).
\tag{26}
$$

真实状态 (10) 在 $H=1$ 时为 $(h,k,\omega+d)$，所以其 d 导数是
$+\partial_\omega$，没有反号或额外的 h 因子。

定义

$$
\boxed{
\mathfrak c(M)=\left.\frac{d}{dd}\right|_{d=0}\mathcal C_{1,d}(M)
=\sum_i a_i(M)[\partial_\omega F_0(S_i^*)].
}
\tag{27}
$$

R105 保证仿射表示为有限 Laurent/多项式表示，所有状态函数光滑，因此该微分在有限真实空间中合法。对 (12)–(14) 求导，得到

$$
\boxed{
\mathsf N[F_0(S)]
=[\partial_\omega F_0(S)]-\mathfrak c(m_0(S)),
}
\tag{28}
$$

$$
\boxed{
\mathsf N[\widehat Q_2(S;u,w)]
=[\partial_\omega\widehat Q_2(S;u,w)]
-\mathfrak c(m_2(S;u,w)),
}
\tag{29}
$$

$$
\boxed{
\mathsf N[F(S)]=[\partial_\omega F(S)]
\quad(F=\bar A_{hh},\bar A_{hk},\bar A_{kk},H_1,H_2,F_{4,0},\ldots,F_{4,4}).
}
\tag{30}
$$

式 (28)–(29) 的负号来自把 (12)–(13) 微分后的 cocycle 项移到另一侧。右侧矩阵是未变换的 $m_j(S)$，所以这里没有再对它作 d 微分。$\partial_\omega$ 只作用于状态函数，不是沿实际路径固定 h、k 时任意指定新的 omega 历史。

令

$$
m_2(S;u,w)=\sum_{i=0}^2m_{2,i}(S)u^iw^{2-i}.
$$

则 (29) 的各个速度系数为
$\mathsf N[F_{2,i}]=[\partial_\omega F_{2,i}]-\mathfrak c(m_{2,i})$。
若省略此项，就会改掉完整字符头部的分母。

## 7. 单一真权数据已经决定完整平移分母

R105 的真实缩放给有限整权分解

$$
U=\bigoplus_\sigma U_\sigma,\qquad
R=\bigoplus_\sigma R_\sigma,\qquad
\mathsf N U_{\sigma+1}\subseteq U_\sigma.
\tag{31}
$$

记对应真实投影为 $\Pi_\sigma$。它作用于完整 profile 函数，不是把几何单项式的 h 次数直接当成原式权。

对每个族 F，定义 $F^{(\sigma)}(S)=\Pi_\sigma F(S)$，并定义单权八矩映射

$$
\mathfrak c_\sigma(M)=
\sum_i a_i(M)\partial_\omega F_0^{(\sigma)}(S_i^*).
\tag{32}
$$

这里及下文可以选任意原式代表；最终只取模 $R_\sigma$ 的类。由同一份十四族的权 $\sigma$ 数据构造

$$
\begin{aligned}
D_0^{(\sigma)}(S)&=
\partial_\omega F_0^{(\sigma)}(S)-\mathfrak c_\sigma(m_0(S)),\\
D_{2,i}^{(\sigma)}(S)&=
\partial_\omega F_{2,i}^{(\sigma)}(S)-\mathfrak c_\sigma(m_{2,i}(S)),\\
D_F^{(\sigma)}(S)&=\partial_\omega F^{(\sigma)}(S)
\quad\text{对最高层十族}.
\end{aligned}
\tag{33}
$$

令 $T_\sigma$ 是十四族 $F^{(\sigma)}$ 全部有限 Laurent/log 状态系数向量的 span，$D_\sigma$ 是 (33) 全部状态系数向量的 span。由于 (33) 只作状态微分和既有系数的标量组合，有
$D_\sigma\subseteq T_\sigma$。如采用带冗余的状态标签，必须先准确归并；不能把新标签的数量当作真实秩。

**定理 2（单权字符头部）。**

$$
\boxed{
U_\sigma=R_\sigma+T_\sigma,\qquad
R_\sigma+\mathsf N U_{\sigma+1}=R_\sigma+D_\sigma.
}
\tag{34}
$$

从而

$$
\boxed{
\mathcal H_\sigma:=
\frac{U_\sigma}{R_\sigma+\mathsf N U_{\sigma+1}}
\ \cong\
\frac{R_\sigma+T_\sigma}{R_\sigma+D_\sigma}.
}
\tag{35}
$$

证明第一式是 R130 的 (9) 经 $\Pi_\sigma$ 投影。对第二式，由 (28)–(30) 及

$$
\Pi_\sigma\mathsf N=\mathsf N\Pi_{\sigma+1}
$$

可得每个族在 Q 中的准确身份

$$
[D_F^{(\sigma)}(S)]
=\mathsf N[\Pi_{\sigma+1}F(S)].
\tag{36}
$$

有限 Laurent/log 状态函数独立，故可逐状态系数比较。R130 使所有
$\Pi_{\sigma+1}F$ 的系数与 $R_{\sigma+1}$ 一起张成
$U_{\sigma+1}$；而 $\mathsf N R_{\sigma+1}\subseteq R_\sigma$。
对这些系数取 $\mathsf N$，(36) 就证明第二式。

因此，构造权 $-2$ 头部时，只需完整十四族的真权 $-2$ 原系数，以及已有的 $R_{-2}$。**不需要另编权 $-1$ 的正规目标，也不需要对那些目标重新实施一次原 profile 平移。** (33) 已准确生成全部所需平移像，低阶修正由同一份静态权 $-2$ 数据给出。

这是一条 span 身份。它不宣称原始 DAG 在 (36) 两侧逐点相同；原代表可以相差真实响应，但 (35) 已把全部 $R_\sigma$ 放入分母。实现仍须保留全部状态支撑及真实函数依赖，不能以零 normal-form 标签代替未经证明的原式关系，也不能把非零 sound 余式当作独立向量。

## 8. 对正字符下一任务的准确用途

U 上权 $\sigma$、杀 R 且满足 $\mathsf N^*\lambda=0$ 的实泛函，与
$\mathcal H_\sigma^*$ 一一对应：从头部取泛函，在其他真权上延为零即可；反向按定义因子化。这只是字符的线性条件。

R145 说明非零正仿射字符若存在，只能有偶整数权。若完整计算证明
$\mathcal H_{-2}=0$，就严格排除权 $-2$ 的非零正字符。若头部非零，不能据此宣称存在正字符；仍须 R140 的同一个八矩乘子 μ，使所有实际开平端路径满足

$$
\int_B(\widetilde\lambda L-\mu m)\,ds\ge0.
\tag{37}
$$

加速度 PSD、固定轴 sharp 条件及有限条路径测试均只给 (37) 的必要条件。它们不能单独替代全部路径、三个时长层和同一个 μ。

若为了排除而使用不完备但 sound 的原式关系，可先建立包含全部真实头部对偶的有限外部候选空间。配合完整生成系数上的非零归一化，在必要正性条件下得到有理不可行证书，仍足以排除该权的真实正字符；可行则仅表示该必要测试尚未排除，不能把形式候选当作 U 上定义良好的正泛函。

R159 的一般 pure 与 balanced 两根共同忠实，可以用于新系数和关系的原式核验；本稿没有假设全部 pure 已属于 R，也没有假设输入相位旋转保持真实成本空间或成本锥。

即使以后排除了全部可能偶权的正字符，R127 直接给出的仍是闭成本锥等于 U。实际有限字、固定基准、完整第四 period 与 ruling 的联合支付，以及高阶收敛和主课题的闭嵌入、reach、幅度条件，仍须分别完成。
