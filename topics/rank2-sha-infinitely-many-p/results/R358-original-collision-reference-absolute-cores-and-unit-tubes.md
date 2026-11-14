# R358：两条原碰撞参考的绝对二次相位、完整 core 及全部普通单位管

日期：2026-11-13。**状态：已证明。** R357 两条实际低次来源
$D=\Theta^2$、$K=\Theta\Theta_\delta=\sigma(3z)/(3\sigma(z))$
的完整普通 core 分别带二次角色 $(-1/p)$、$(-2/p)$。
绝对相位由原 CM7、CM13 的完整纤维迹、对称 Heisenberg lift 和两个已付原来源锚定。
因而 R357 的两条单相位碰撞管对**每个**普通 $p>7$ 都有单位质量，
它们的所有深度及 primitive 双非单位 carry 也全部准确给出。
此处的单位系数是原中央观察的无损系数，不单独断言原 $J'_S(0)$ 非零。

## 1. 原对象和主结论

同 R316、R350、R357，固定
$$
E_b:y^2=x^3+b,\quad b=17,\quad
\omega^2+\omega+1=0,\quad\delta=1+2\omega,\quad
\Theta=x\sigma^2,\quad X=x^3,
$$
$$
D=\Theta^2,\qquad
K=\Theta(z)\Theta(\delta z)
   =\sigma^8x(X+4b)=\frac{\sigma(3z)}{3\sigma(z)}.
\tag{1}
$$
最后一个等式是两次原 norm3 identity
$\sigma(\delta z)=\delta\sigma(z)\Theta(z)$ 的直接结果，
因为 $\delta^2=-3$。
$D,K$ 均 $\mu_6$ 不变、原点质量一，分别是 degree 四、八的实际全纯来源。

令 $p>7$、$p\equiv1\pmod3$，采用原目标的普通嵌入与周期：
$$
\pi=\psi_{17}(\mathfrak p),\quad \pi\bar\pi=p,\quad
\varepsilon=\psi_0(\mathfrak p)/\psi_{17}(\mathfrak p)\in\mu_6,
\quad \kappa=p/\bar\pi^2 .
\tag{2}
$$
$\psi_0$ 是 $E_0:y^2=x^3+1$ 的实际角色。
记
$$
\chi_-(p)=\left(\frac{-1}{p}\right),\qquad
\chi_{-2}(p)=\left(\frac{-2}{p}\right),
$$
$$
\boxed{
\lambda_D=\frac{\varepsilon\chi_-(p)}{\bar\pi},\qquad
\lambda_K=\frac{\varepsilon\chi_{-2}(p)}{\bar\pi}.
}
\tag{3}
$$
原测度的变换统一为
$G(\Omega_p\log(1+T))$，不改变原微分和正式群。

**定理。** 完整原测度满足
$$
\boxed{
\nu_D|_{p\mathbf Z_p}=\lambda_D[\kappa]_*\nu_D,\qquad
\nu_K|_{p\mathbf Z_p}=\lambda_K[\kappa]_*\nu_K .
}
\tag{4}
$$
而且
$$
\boxed{1-\lambda_D,\quad1-\lambda_K\in\mathcal O^\times.}
\tag{5}
$$
以下先在 $b=1$ 支付全部绝对相位，再用原正式同构传回 $b=17$。

## 2. 同一原 CM 迹及真实锚

在 $E_0$ 上记 $\sigma_0,x_0,y_0,\Theta_0$，暂省略下标。
设 $\Gamma=\operatorname{Per}(E_0,dz)$，
$$
\mathcal S_N=\sigma^NL(NO),\qquad N=4,8.
$$
对奇范数 CM 元素 $a$，用首项常数为 $a$ 的原 division 函数
$r_a=\sigma(az)/\sigma(z)^{Na}$，以及 R300 的实际迹
$$
\mathscr M_a(\sigma^Nf)
=\sigma^N\operatorname{Tr}_{[a]}
       \left[(r_{\bar a}/r_a)^N f\circ[\bar a]\right].
\tag{6}
$$
R300 的逐支正式群证明给
$$
T_{p,0}=\frac{\bar\pi_0}{p}\mathscr M_{\pi_0}
       =\pi_0^{-1}\mathscr M_{\pi_0},\qquad
\pi_0=\psi_0(\mathfrak p).
\tag{7}
$$
同一个证明保持完整的 $\mathcal S_4,\mathcal S_8$。
R316 已付 $T_{p,0}\sigma=T_{p,0}\Theta$ 的各自本征标量一。
乘变量二与完整 $p$-core 交换，所以两条实际锚为
$$
\boxed{
\mathscr M_{\pi_0}\sigma(2z)=\pi_0\sigma(2z)
 \quad\text{于 }\mathcal S_4,\qquad
\mathscr M_{\pi_0}\Theta(2z)=\pi_0\Theta(2z)
 \quad\text{于 }\mathcal S_8 .
}
\tag{8}
$$
这里分别使用原 odd 线和原 even 线，没有拿一个在别的 degree 的
质量作未支付的标量。

采用 R300 的对称 lift
$$
(\mathsf T_vG)(z)=e^{-N\eta_v(z+v/2)}G(z+v),
\qquad v\in N^{-1}\Gamma.
$$
它满足原中心相位、$2\Gamma$ 周期以及完整交织
$$
\mathscr M_a\mathsf T_v
           =\mathsf T_{a\bar a^{-1}v}\mathscr M_a,
\tag{9}
$$
其中右侧参数按模 $2N$ 读取，不能只模 $N$。
两个标准平移的交换子是 primitive $N$ 次根，
由循环基直接知整个 $N$ 维表示不可约。

因此具有同一 $g=a/\bar a\bmod2N$ 的非零交织算子只差一个标量。
若再固定 (8) 的同一非零锚，标量就是一。
同样，两个归一交织算子的乘积实现两个 $g$ 的乘积，并仍固定锚。
所以归一后的有限作用是一个**真正表示**，无需假设未付的
同度 trace 乘法或在不同空间之间转移标量。

## 3. 两个生成元的完整原纤维迹

取
$$
a_7=3+\omega,\qquad a_{13}=4+\omega,
$$
其原 primary Frobenius 生成元为
$$
\varpi_7=\omega a_7=-1+2\omega,\qquad
\varpi_{13}=-\omega^2a_{13}=3+4\omega.
\tag{10}
$$
它们都 $\equiv1\pmod{2\delta}$，范数分别为七、十三。

在 $b=1$ 的整个 $\mathcal S_8^{\mu_6}$ 中取基
$$
V=\sigma^8x,\qquad W=\sigma^8x^4.
$$
则 $K=4V+W$、$\Theta(2z)=-8V+W$。
两次完整纤维迹均给
$$
\boxed{
\left.\mathscr M_{a_7}\right|_{\mathcal S_8^{\mu_6}}
=\varpi_7 R,\qquad
\left.\mathscr M_{a_{13}}\right|_{\mathcal S_8^{\mu_6}}
=\varpi_{13}R,\qquad
R=
\begin{pmatrix}
1/3&-16/3\\
-1/6&-1/3
\end{pmatrix}.
}
\tag{11}
$$
$R(4,1)^t=-(4,1)^t$，$R(-8,1)^t=(-8,1)^t$。

在 $\mathcal S_4$ 的唯一 $\mu_6$ 不变线 $D=\sigma^4x^2$ 上，准确为
$$
\boxed{
\mathscr M_{a_7}D=-\varpi_7D,\qquad
\mathscr M_{a_{13}}D=\varpi_{13}D.
}
\tag{12}
$$
原 odd 锚也由同一完整纤维计算支付：
$$
\boxed{
\mathscr M_{a_7}(\sigma^4y)=a_7\,\sigma^4y,\qquad
\mathscr M_{a_{13}}(\sigma^4y)=-a_{13}\,\sigma^4y .
}
\tag{13}
$$
$\sigma(2z)=-2\sigma^4y$。

若 $G(uz)=u^kG(z)$、$u\in\mu_6$，直接在 (6) 中换原纤维给
$$
\boxed{\mathscr M_{ua}G=u^{-2k}\mathscr M_aG.}
\tag{14}
$$
确切地，$r_{ua}=u r_a$、$r_{\bar u\bar a}=\bar u r_{\bar a}$，
而 $f(\bar u z)=u^{N-k}f(z)$；连同输出 $\sigma^N$ 的单位变换，
总因子就是 $u^{-2k}$。
所以 (11)、(12) 的 $k=0$ 来源不变；(13) 在
$u=\omega,-\omega^2$ 下分别成为 $\varpi_7,\varpi_{13}$。
这支付了 (8) 的固定生成元锚，包含所有单位相位。

### 3.1 可复算的有限迹公式

为使 (11)–(13) 不依赖任何小数识别，给出它们的完整有限输入。
原 division 多项式为
$$
r_{a_7}=a_7P_7(x),\qquad
P_7=x^3+\frac{4+12\omega}{7},
$$
$$
r_{a_{13}}=a_{13}P_{13}(x),\qquad
P_{13}=x^6+(8+12\omega)x^3+\frac{64+48\omega}{13}.
\tag{15}
$$
它们来自 R297 的真实 CM7、CM13 division，保留首项常数。
对 $n=Na$、$P=P_a$，置
$$
U_a=nxP^2-4(x^3+1)(P''P-P'^2)-6x^2P'P,\qquad
V_a=a^2P^2 .
\tag{16}
$$
原恒等式 $-\partial_z^2\log\sigma(az)=a^2x(az)$ 给
$x(az)=U_a/V_a$。
对目标横坐标 $h=1,2$，完整 $[a]$ 纤维的横坐标代数是
$$
f_h(x)=U_a(x)-hV_a(x),
\tag{17}
$$
它是 degree $n$ 的首一可分多项式。
原待迹函数是
$$
R_{N,j}=
 \left(\frac{\bar a}{a}\frac{\bar P}{P}\right)^N
             \left(\frac{U_{\bar a}}{V_{\bar a}}\right)^j.
\tag{18}
$$
其完整迹可由
$$
\operatorname{Tr}(R_{N,j})
=[x^{n-1}]\bigl(R_{N,j}f_h'\bmod f_h\bigr)
\tag{19}
$$
直接在 $\mathbf Q(\omega)[x]/(f_h)$ 中读取。
原 $N=8,j=1,4$ 的结果为
$$
\begin{array}{c|cc}
h&\operatorname{Tr}(R_{8,1})/\varpi_a&
                 \operatorname{Tr}(R_{8,4})/\varpi_a\\ \hline
1&1/6&-17/3\\
2&-2&-16
\end{array}
\tag{20}
$$
对 $a=a_7,a_{13}$ 相同。
两条基的值是 $(h,h^4)$，其在 $h=1,2$ 的行列式为十四；
因此 (20) 唯一给出完整矩阵 (11)。
实际 $\mu_6$ 不变块只有这两维，所以无需猜测更高项。
$N=4,j=2$ 在两个纤维除以 $h^2$ 后分别为
$-\varpi_7,+\varpi_{13}$，给 (12)。

odd 锚不能删去 $y$ 比。真实比是
$$
\frac{y(\bar aP)}{y(aP)}
=\frac a{\bar a}\frac{(U_{\bar a}/V_{\bar a})'}
                         {(U_a/V_a)'} .
\tag{21}
$$
在 (19) 中，$f_h'$ 恰消掉 (21) 的纤维分母，所得准确系数是
$$
\frac1n[x^{n-1}]
 \left(\frac{U_{\bar a}'V_{\bar a}-U_{\bar a}V_{\bar a}'}
                   {P_a^2}\bmod f_h\right).
\tag{22}
$$
它在 $h=1,2$ 都分别等于 $a_7,-a_{13}$。
(15)–(22) 只需
$(a+b\omega)(c+d\omega)=(ac-bd)+(ad+bc-bd)\omega$
和有限多项式除法。本次计算在有理 BigInt 的 $\mathbf Q(\omega)$ 中完成；
它是固定特征零矩阵的准确计算，没有扫描目标素数。

## 4. 原完整有限群与绝对二次角色

对 $E_0$ 的每个实际 $\pi_0$，有
$$
\pi_0\equiv1\pmod{2\delta}.
$$
故在模十六上，全部可能的实际 ratio 落入
$$
H_0=\{a/\bar a\bmod16:\ a\equiv1\pmod2\}.
\tag{23}
$$
集合 $a\equiv1\pmod2$ 有六十四个可逆元素。
ratio 的核是八个奇有理标量：写 $a=A+B\omega$，
$a=\bar a$ 当且仅当 $B\delta=0\bmod16$，而 $\delta$ 是二进单位。
所以 $|H_0|=8$。

(10) 给两个准确生成元
$$
g_7=11+8\omega,\qquad g_{13}=13+8\omega\pmod{16},
$$
$$
g_7^2=g_{13}^2=9,\qquad g_7g_{13}=-1,\qquad
H_0=\langle g_7,-1\rangle\simeq C_4\times C_2.
\tag{24}
$$
这八个元素全不同，因而已覆盖 (23) 的完整像。
对于 $\mathcal S_4$，将此群进一步模八即可；
对于 $\mathcal S_8$，保留整个模十六，包括中心相位。

用第2节的真实锚分别归一 $\mathscr M_{\pi_0}/\pi_0$。
(11)、(12) 给两条特征在 $(g_7,g_{13})$ 上的值
$$
\begin{array}{c|cc}
 &g_7&g_{13}\\ \hline
D&-1&+1\\
K&-1&-1 .
\end{array}
\tag{25}
$$
由锚定后的 Heisenberg 唯一性，这两行决定所有实际 $\pi_0$ 的作用，
而非只决定七和十三两个素数。

范数 $Na\bmod8$ 由 $g=a/\bar a\bmod16$ 唯一决定：
同一 ratio 的两个代表相差模十六的奇有理单位，其范数是奇数平方，
模八为一。因此
$$
N(g_7)\equiv7,\qquad N(-1\text{ as ratio})\equiv3\pmod8.
$$
第二式可取代表 $\varpi_7\varpi_{13}$，范数 $91\equiv3\pmod8$。
完整表为
$$
\begin{array}{c|c|c|c|c}
e&j&g_7^e(-1)^j&Na\bmod8&(\chi_D,\chi_K)\\ \hline
0&0&1&1&(1,1)\\
1&0&11+8\omega&7&(-1,-1)\\
2&0&9&1&(1,1)\\
3&0&3+8\omega&7&(-1,-1)\\
0&1&15&3&(-1,1)\\
1&1&5+8\omega&5&(1,-1)\\
2&1&7&3&(-1,1)\\
3&1&13+8\omega&5&(1,-1).
\end{array}
\tag{26}
$$
所以
$$
\chi_D(g)=\left(\frac{-1}{Na}\right),\qquad
\chi_K(g)=\left(\frac{-2}{Na}\right).
\tag{27}
$$
在实际 $Na=p$ 上，得到
$$
\boxed{
T_{p,0}D=\chi_-(p)D,\qquad
T_{p,0}K=\chi_{-2}(p)K.
}
\tag{28}
$$
(28) 同时支付标量、符号及完整有限相位，不依赖新的 Katz 平方选择。

## 5. 原周期和六次扭转传回 $E_{17}$

令 $\theta=17^{1/6}$，并采用 R316 的真实正式同构与普通嵌入。
有
$$
\Omega_{p,0}=\theta\Omega_p,\qquad
D_b(z)=D_0(\theta z),\qquad
K_b(z)=K_0(\theta z).
\tag{29}
$$
这些等式来自 $x_b(z)=\theta^2x_0(\theta z)$、
$\sigma_b(z)=\theta^{-1}\sigma_0(\theta z)$，不是在测度变量上任意乘 $\theta$。

又
$$
\pi_0=\varepsilon\pi,\qquad
\bar\pi_0=\varepsilon^{-1}\bar\pi,\qquad
p/\bar\pi_0^2=\varepsilon^2\kappa .
$$
两条原来源的 $\mu_6$ 型都是零，所以
$[\varepsilon^2]_*\nu_D=\nu_D$、
$[\varepsilon^2]_*\nu_K=\nu_K$。
因此 (28) 的完整 $p$ 限制准确传为 (3)、(4)。
没有漏掉相位 $\varepsilon$ 或改变 $Y$ 的原周期。

## 6. 两个环带质量对全部普通素数为单位

(3) 也有一个明确的椭圆曲线解释，仅用于支付单位性：
$$
E_-:y^2=x^3-1,\qquad E_{-2}:y^2=x^3-8.
\tag{30}
$$
它们分别是 $E_0$ 的 $-1,-2$ 二次扭曲。
真实 Frobenius 因而为
$\chi_-(p)\pi_0$、$\chi_{-2}(p)\pi_0$，给
$$
\lambda_D=1/\bar\pi_-,\qquad
\lambda_K=1/\bar\pi_{-2}.
\tag{31}
$$
不需要假设这两条曲线的中央导数或高度。

两条曲线分别有有理二挠点 $(1,0)$、$(2,0)$。
因此在每个好奇素数 $p$，其 $a_p$ 都是偶数。
若 $1-\bar\pi_*^{-1}$ 在原普通位非单位，
则 $a_p=\pi_*+\bar\pi_*\equiv1\pmod p$。
对 $p>7$，Hasse 界 $|a_p|\le2\sqrt p<p-1$
迫 $a_p=1$，与偶性矛盾。
这证明 (5) 对全部本篇普通素数成立，而不需删除稀薄异常集。

## 7. 全部深度、tame 和不可删除的质量尾

迭代 (4)，对 $G=D,K$ 得
$$
\nu_G|_{p^n\mathbf Z_p}=\lambda_G^n[\kappa^n]_*\nu_G,\qquad
\nu_G(p^n\mathbf Z_p)=\lambda_G^n.
\tag{32}
$$
记 $d=p-1$，原单位 Mellin 为
$$
M_{G,\ell}(u)=\int_{\mathbf Z_p^\times}
             \omega_p(x)^\ell\langle x\rangle^{du}\,d\nu_G(x).
$$
归一第 $n$ 环带变量为 $x/p^n$，其完整 Mellin 为
$$
\boxed{
M^{[n]}_{G,\ell}(u)
=\lambda_G^n\omega_p(\bar\pi)^{-2n\ell}
          \langle\bar\pi\rangle^{-2ndu}M_{G,\ell}(u).
}
\tag{33}
$$
中央导数完整保留
$$
M^{[n]\prime}_{G,\ell}(0)
=\lambda_G^n\omega_p(\bar\pi)^{-2n\ell}
 \left(M'_{G,\ell}(0)
       -2nd\log_p(\bar\pi)M_{G,\ell}(0)\right).
\tag{34}
$$
principal 原质量 $M_{G,0}(0)=1-\lambda_G$ 是已证单位，
但本篇没有给未知的 $M'_{G,0}(0)$ 随意赋值。

由于 $\lambda_G$ 是单位，全部深域的质量不趋于零。
准确有限重构必须写成
$$
\boxed{
\nu_G=\sum_{j=0}^{M-1}\lambda_G^j[\kappa^j]_*\nu_G^\times
                +\lambda_G^M[\kappa^M]_*\nu_G .
}
\tag{35}
$$
最后一项的质量为 $\lambda_G^M$，不能删除。
若需要弱收敛无穷式，先以
$\nu_G^\times-(1-\lambda_G)\delta_0$ 作质量零修正，
再加回 $\delta_0$，与 R316 的原规范一致。
这保留了本篇所有碰撞质量所依赖的真实非单位边界。

## 8. 原碰撞管的明确单位系数和 primitive carry

R357 的真实坐标是
$$
P=\delta(L_r+L_s),\qquad Q=\delta(L_r-L_s),
$$
其整个联合在分别 $\mu_6$ 不变测试下准确为
$\nu_K\otimes\nu_D$。
因此其记号 $k_a,d_a$ 现在全部确定为
$$
\boxed{k_a=\lambda_K^a,\qquad d_a=\lambda_D^a.}
\tag{36}
$$
对 $N\ge a\ge1$，两条原相位的完整质量为
$$
\boxed{
\begin{aligned}
e_{1;a,N}&=\lambda_K^a\lambda_D^N,&
q_{1,N}&=(1-\lambda_K)\lambda_D^N,\\
e_{-1;a,N}&=\lambda_K^N\lambda_D^a,&
q_{-1,N}&=(1-\lambda_D)\lambda_K^N .
\end{aligned}}
\tag{37}
$$
这些 $q_{\pm1,N}$ 对所有本篇素数和所有 $N\ge1$ 都是单位。

设 $t_p=\varepsilon^3p/\bar\pi^3$ 是 R350 原五输入五次权的收缩参数。
它的全部 primitive-input 双非单位边界也准确是
$$
\boxed{
e^{\mathrm{prim}}_{1;a,N}
=\lambda_K^{a-1}\lambda_D^{N-1}
                       (\lambda_K\lambda_D-t_p^5).
}
\tag{38}
$$
因为 $v_p(t_p^5)=5$，(38) 本身对所有 $a,N$ 都为单位。
这说明该 carry 从来不是“全部输入深”的可忽略尾：
其非单位输出由原单位输入的相加碰撞产生，并且原质量被完整保留。
与 (35) 一样，不能以实测度式的可数可加性推断深管质量趋零。

对原未缩放的 $Y$、全部 tame $\ell$，
$$
\boxed{
J_{\mathcal H_{1,N};\ell}(u)
       =(1-\lambda_K)\lambda_D^N J_{S,\ell}(u),\qquad
J_{\mathcal H_{-1,N};\ell}(u)
       =(1-\lambda_D)\lambda_K^N J_{S,\ell}(u).
}
\tag{39}
$$
尤其两个原中央导数都是 $J'_S(0)$ 的明确单位倍数。
这里系数不依赖 Mellin 权，所以不另添参考斜率；
(33)、(34) 的非零质量尺度项仍只在实际归一辅助环带时出现。

R350/R357 的原叶深度分解现在成为
$$
\mathcal L_p(\mathcal D_{\boldsymbol n})
+\mathcal L_p(\mathcal E_0)+\sum_j\mathcal L_p(\mathcal E_j)
       =(1-\lambda_K)\lambda_D^N J'_S(0).
\tag{40}
$$
右端已经完全显式且无损；左端仍是同一原叶核的全部补项。
原叶限制并不都是 $P,Q$ 的函数，
所以本篇没有从 R339 的某个非零子域直接推断整个右端非零。
后续仍需在 (40) 的真实补域上取得新的联合域控制。

### 引用

- [R297：原 CM7/CM13 division 与同一 sigma 规范](R297-jzero-actual-cm13-mass-kernel-cm7-product-and-angular-source.md)。
- [R300：完整原 theta 迹、对称 lift 与绝对 core 规范](R300-jzero-full-theta-prime-core-and-single-euler-measure.md)，特别 §§2–2.1。
- [R316：同一原 sigma/Theta 的完整 core 和扭转周期](R316-jzero-low-degree-original-cores-and-complete-four-factor-carry.md)，特别 §§3–5。
- [R350：对角双辅助及原碰撞、叶补域](R350-original-diagonal-pair-six-phase-collision-and-leaf-complement.md)。
- [R357：和差四项完整联合与实际边界消元](R357-original-pair-sum-difference-joint-and-collision-boundary.md)。
