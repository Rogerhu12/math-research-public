# R344：两个重叠原辅助坐标的整条因子化、挠点零及五输入收缩核

日期：2026-11-13。**状态：已证明。** 对 R341 两个相交于一个原输入的三元组，直接取其联合坐标并分别作 $\mu_6$ 投影，整个输出始终是原固定来源 $S$ 的倍数。证明使用真实 $2,6,7$ 挠点零和低次数 theta 空间，涵盖全部辅助权，并非由有限 Taylor 样本推断。对应的完整有界测度准确分解为 $\nu_S\otimes\Xi$；$\Xi$ 质量一、两条边缘均为原 $\rho_2$，但两坐标不独立。$\Xi$ 还具有一个五个原 sigma 输入、五次权的准确核，全部输入在 $p$ 时给 $p^5$ 收缩与完整尾。任意分别 $\mu_6$ 不变的相关辅助域因此真正返回原完整中央函数。原叶深度域的其余限制仍须保留。

## 1. 原来源与两个真正相交的坐标

固定
$$
E:y^2=x^3+b,\qquad b=17,\qquad
\delta^2=-3,\quad\omega=(\delta-1)/2,\quad
\gamma=(5+\delta)/2,
$$
以及 R316、R333 的同一原 sigma、普通测度 $\nu$ 和周期 $\Omega=\Omega_p$。
普通素数始终满足 $p>7$、$p\equiv1\pmod3$。

原六尺度、原目标和相加输出为
$$
\boldsymbol c=(1,2,\delta,2\delta,\gamma,\bar\gamma)^t,\qquad
S=-\frac1{84}\prod_{i=1}^6\sigma(c_i z),\qquad
Y=\sum_i c_iX_i.
\tag{1}
$$
$S=z^6+\cdots$，并且 R297 已准确证明
$$
\boxed{
S=\sigma^{34}x^2
 (X+b)(X-8b)\left(X^2-\frac{4b}{7}X+\frac{16b^2}{7}\right),
\qquad X=x^3.
}
\tag{2}
$$
取 R341 的两条原单位关系
$$
\boldsymbol r=(1,\omega^2,1,0,0,0)^t,\qquad
\boldsymbol s=(1,0,0,-\omega^2,-\omega,0)^t,
\tag{3}
$$
以及两个实际输入坐标
$$
L_r=\delta^{-1}\boldsymbol r^*\boldsymbol X,\qquad
L_s=\delta^{-1}\boldsymbol s^*\boldsymbol X.
\tag{4}
$$
这里
$$
\boldsymbol c^t\boldsymbol r=\boldsymbol c^t\boldsymbol s=0,\qquad
\boldsymbol r^*\boldsymbol s=1.
$$
两个三元组分别为 $123$ 和 $145$，真实地重叠于第一个输入。
第六个原因子完全不进入这两个辅助坐标。

令 $\mathsf P_{\mathrm{aux}}$ 在联合输出的 $L_r,L_s$ 两坐标上分别作
$\mu_6$ 平均，保持原 $Y$ 不动。它不是先后在原六输入上作 R341 的
$\Pi_r,\Pi_s$；后两者会移动彼此的辅助坐标，且已知有非零源交换差。

## 2. 原整条三变量函数与固定 theta 空间

在复变量中写
$$
\mathcal F_{\boldsymbol c}(z;v,w)
=-\frac1{84}\prod_{i=1}^6
 \sigma\left(c_i z+\frac{\bar r_i v+\bar s_i w}{\delta}\right),
$$
$$
\mathcal A_{\boldsymbol c}(z;v,w)
=\frac1{36}\sum_{\zeta,\eta\in\mu_6}
               \mathcal F_{\boldsymbol c}(z;\zeta v,\eta w).
\tag{5}
$$
以下证明整个原恒等式
$$
\boxed{\mathcal A_{\boldsymbol c}(z;v,w)=S(z)\Psi(v,w)}
\tag{6}
$$
且明确支付 $\Psi$ 的原测度和全部常数。

### 2.1 周期、Gaussian 和原点质量

对原等调和晶格，reduced sigma 的 CM 准周期满足
$\eta(a\lambda)=\bar a\,\eta(\lambda)$。
因此 $z\mapsto z+\lambda$ 时，(5) 的两个交叉项分别含
$$
\sum_i\bar c_i\bar r_i=\overline{\boldsymbol c^t\boldsymbol r}=0,
\qquad
\sum_i\bar c_i\bar s_i=0.
\tag{7}
$$
所有辅助 Gaussian 准确消失。原尺度的 sigma division 身份表明其总线丛是
$\mathcal O(34O)$，因为 $\sum N(c_i)=34$；这与 (1) 的真实来源相同。
所以对固定 $v,w$，(5) 是原 $\sigma^{34}L(34O)$ 中的整个截面。

同时 $\sigma(\zeta z)=\zeta\sigma(z)$，六个因子的总相位为 $\zeta^6=1$。
分别对 $v,w$ 平均后，得到
$$
\mathcal A_{\boldsymbol c}(\zeta z;v,w)
                      =\mathcal A_{\boldsymbol c}(z;v,w).
\tag{8}
$$
第六因子是未移位的 $\sigma(\bar\gamma z)$，所以 $z=0$ 的值为零。
原 $\mu_6$ 不变、质量零的 degree 三十四空间准确是
$$
\boxed{
\sigma^{34}x^2\,\{P(X):\deg P\le4\}.
}
\tag{9}
$$
其五个原基列也可写成纯正乘积
$$
F_j=\sigma^{30-6j}\Theta^{2+3j},\qquad 0\le j\le4.
\tag{10}
$$
因此这里没有扩大到一个带自由 theta 连接的环境。

## 3. 搬移到挠点时，全部辅助相位保持不变

下面的引理支付后文每一次模 CM 理想的换代表。

**真实周期搬移引理。** 设 $\boldsymbol u\in\mathcal O_K^6$ 满足
$$
\boldsymbol u^t\boldsymbol r=\boldsymbol u^t\boldsymbol s=0,\qquad
c_i-u_i=\alpha d_i,\quad d_i\in\mathcal O_K.
$$
若 $T\in E[\alpha]$，则存在一个非零常数
$e_{\boldsymbol c,\boldsymbol u}(T)$，不依赖 $v,w$，使
$$
\boxed{
\mathcal A_{\boldsymbol c}(T;v,w)
=e_{\boldsymbol c,\boldsymbol u}(T)\,
                  \mathcal A_{\boldsymbol u}(T;v,w).
}
\tag{11}
$$
右边仍由 (5) 定义，保留同一六个原 sigma 与同一两个辅助系数。

证明：选定复提升 $T$，令 $\Lambda=\alpha T\in\Gamma$。
逐因子使用原 sigma 准周期式。写其符号为 $\epsilon_\Gamma$，完整常数是
$$
e_{\boldsymbol c,\boldsymbol u}(T)
=\prod_i\epsilon_\Gamma(d_i\Lambda)\,
 \exp\left(\eta(\Lambda)
       \left[T\sum_i\bar d_i u_i+
                    \frac{\Lambda}{2}\sum_i|d_i|^2\right]\right).
\tag{12}
$$
辅助 $v$ 的指数是
$\eta(\Lambda)\overline{\sum d_i r_i}\,v/\delta$，而
$\sum d_i r_i=\alpha^{-1}(\boldsymbol c-\boldsymbol u)^t\boldsymbol r=0$。
$w$ 同理。因此 (12) 是整个、非零且与两个辅助变量无关的真实因子。
它也不因 (5) 的两次单位平均而改变，这证明 (11)。$\square$

这里只用非零常数传递零点；最终整个来源的归一由原 $s_6=1$ 决定。
没有把单个平移项的非恒定 Gaussian 无条件删掉。

## 4. 真正的低次换代表与四组固定零

使用以下三个明确的原 CM 向量：
$$
\begin{aligned}
\boldsymbol u_\gamma&=(1,\omega^2,\omega^2,\omega,0,-\omega^2),\\
\boldsymbol u_2&=(1,0,-1,0,\omega^2,\omega),\\
\boldsymbol u_6&=(1,2,\delta,0,\omega^2,\omega).
\end{aligned}
\tag{13}
$$
它们全部同时垂直于 $\boldsymbol r,\boldsymbol s$。
准确同余与次数为
$$
\begin{array}{c|c|c}
\text{向量}&\text{原同余}&\sum N(u_i)\\\hline
\boldsymbol u_\gamma&\boldsymbol c\bmod\gamma&5\\
\boldsymbol u_2&\boldsymbol c\bmod2&4\\
\boldsymbol u_6&\boldsymbol c\bmod2\delta&10
\end{array}
\qquad
\boldsymbol u_6\equiv\boldsymbol u_2\pmod2.
\tag{14}
$$
证书列出每个差向量除以对应 CM 元素后的整系数，
并逐项核定引理中的两个交叉和为零。

对这些向量，所有非零尺度都是 CM 单位或 $2,\delta$。
原 sigma 的单位、倍点及 norm3 division 身份直接支付各自的
$\mathcal O(NO)$ 线丛。它们的第六因子仍未移位且尺度非零，
所以其 $\mu_6$ 平均在 $z=0$ 的质量也为零。

### 4.1 degree 四与五的质量零空间都是零

$L(NO)$ 的实际基为 $x^a$ 及 $yx^a$，极阶分别为 $2a$、$3+2a$。
$\sigma^Nx^ay^e$ 的 $\mu_6$ 型为 $N-2a-3e$。
于是
$$
\begin{array}{c|c|c}
N&\mu_6\text{ 不变空间的基}&\text{质量零子空间}\\\hline
4&\sigma^4x^2&0\\
5&\sigma^5xy&0\\
10&\sigma^{10}x^2,\ \sigma^{10}x^5&
                          \mathbf C\,\sigma^{10}x^2 .
\end{array}
\tag{15}
$$
前两行的唯一基列在原点的质量分别为 $1,-1$。
因此
$$
\boxed{\mathcal A_{\boldsymbol u_\gamma}
                 =\mathcal A_{\boldsymbol u_2}=0}
\tag{16}
$$
作为 $z,v,w$ 的整个函数恒等成立。

由 (11)，原 $\mathcal A_{\boldsymbol c}$ 在全部 $E[\gamma]$ 与 $E[2]$
点上为零。另一方面它仍含未移位因子 $\sigma(\bar\gamma z)$，
所以全部 $E[\bar\gamma]$ 零也直接保留。

### 4.2 degree 十的最后一条线也被真实二挠零杀掉

由 (15)，
$$
\mathcal A_{\boldsymbol u_6}(z;v,w)
                     =a(v,w)\sigma(z)^{10}x(z)^2.
$$
但 $\boldsymbol u_6\equiv\boldsymbol u_2\pmod2$，且两个向量都满足原正交关系。
再用一次 (11)、(16)，该整个截面在每个非零二挠点为零。
在那里 $\sigma^{10}x^2$ 非零，所以 $a(v,w)=0$。因此
$$
\boxed{\mathcal A_{\boldsymbol u_6}=0.}
\tag{17}
$$
由 $\boldsymbol c\equiv\boldsymbol u_6\bmod2\delta$，
原 $\mathcal A_{\boldsymbol c}$ 也保留全部 $E[2\delta]$ 零。

这一步没有仅按次数十断言空间为零：实际质量零线先保留，
再由原二挠点值将它严格消掉。

### 4.3 四个不同的角根准确给回原 $S$

由 (9)，写
$\mathcal A_{\boldsymbol c}=\sigma^{34}x^2P_{v,w}(X)$，$\deg P_{v,w}\le4$。
非零二挠点有 $X=-b$。
$E[2\delta]$ 中不属于 $E[2]\cup E[\delta]$ 的六点有 $X=8b$：
原倍点式
$$x(2z)=\frac{x(X-8b)}{4(X+b)}$$
将这些点送到 $x=0$ 的非零 $\delta$ 挠点，反向计数也给全部六点。

原 CM7 division 身份为
$$
\frac{\sigma(\gamma z)}{\sigma(z)^7}
=\gamma\left(X+\frac{-2+6\delta}{7}b\right),
\qquad
\frac{\sigma(\bar\gamma z)}{\sigma(z)^7}
=\bar\gamma\left(X+\frac{-2-6\delta}{7}b\right).
\tag{18}
$$
故另外两组非零七挠零给
$$X=\frac{2-6\delta}{7}b,\qquad X=\frac{2+6\delta}{7}b.$$
四个角根两两不同。$P_{v,w}$ 的次数至多四，所以它必是
$$
(X+b)(X-8b)\left(X^2-\frac{4b}{7}X+\frac{16b^2}{7}\right)
$$
的倍数。结合 (2) 即得整个 (6)。

此证明使用全部真实挠点零与有限维线丛，故 (6) 对任意辅助权成立。
下面的低阶系数只用来计算一个明确的原辅助矩，不作为全因子化的依据。

## 5. 完整辅助函数与原有界联合测度

由 $S=z^6+\cdots$，
$$
\boxed{\Psi(v,w)=[z^6]\mathcal A_{\boldsymbol c}(z;v,w),\qquad
\Psi(0,0)=1.}
\tag{19}
$$
它也有一个没有未知比例常数的有限表达。
第六因子在取 $z^6$ 时只能贡献 $\bar\gamma z$，
因为 sigma 在零点的非零阶恰为 $1\bmod6$。
写 $a_i=\bar r_i/\delta$、$b_i=\bar s_i/\delta$，则
$$
\boxed{
\Psi(v,w)=
-\frac{\bar\gamma}{84\cdot36}
\sum_{\zeta,\eta\in\mu_6}
\sum_{\substack{n_1+\cdots+n_5=5\\n_i\ge0}}
\prod_{i=1}^5
 \frac{c_i^{n_i}}{n_i!}\,
 \sigma^{(n_i)}(a_i\zeta v+b_i\eta w).
}
\tag{20}
$$
这些是原 sigma 的至多五阶导数，所有相位仍是 (3) 的实际相位。

在原普通测度上，令
$$
\eta_6=-\nu^{\otimes6}/84,\qquad
\mathcal J=\mathsf P_{\mathrm{aux}}(Y,L_r,L_s)_*\eta_6,
$$
并直接定义
$$
\boxed{
\Xi=\frac1{6!\Omega^6}\,
      (\operatorname{pr}_{L_r,L_s})_*(Y^6\mathcal J).
}
\tag{21}
$$
$6!\Omega^6$ 对本篇素数是单位，所以 $\Xi$ 是一个有界整的原二维测度。
使用 $\Omega$ 归一的 Laplace 变换，(21) 的变换恰为 (19)。
由整个 (6) 及有界测度变换的单射性，得到
$$
\boxed{\mathcal J=\nu_S\otimes\Xi.}
\tag{22}
$$
这里先证明的是完整三变量测度身份，因而可测试开闭域、所有原输出环带和全部 tame，
不局限于正整数矩。

$\Xi$ 的质量为一。由 R341 单辅助联合身份，两个边缘都准确等于
$$
\boxed{
(\operatorname{pr}_1)_*\Xi=(\operatorname{pr}_2)_*\Xi
=\rho_2=-[\delta^{-1}]_*\nu_C,\qquad C=y\sigma^3.
}
\tag{23}
$$
R341 的完整 core 给
$\rho_2|_p=\lambda_C[\kappa]_*\rho_2$、
$\lambda_C^6=\bar\pi^{-6}$。
(23) 不表示两个辅助变量独立。

## 6. 五个原输入和真实 $p^5$ 收缩

公式 (21) 可进一步消去未移位的第六输入。
置
$$
Y_5=\sum_{i=1}^5c_iX_i.
$$
$\nu$ 的质量为零，且六阶以下只有第一矩 $\mu_1=\Omega$ 非零。
因此对原 $(Y_5+\bar\gamma X_6)^6$ 积分时，只有 $X_6$ 的一次项留下。
准确得到
$$
\boxed{
\Xi=
-\frac{\bar\gamma}{84\cdot5!\Omega^5}
\mathsf P_{\mathrm{aux}}(L_r,L_s)_*
                       \bigl(Y_5^5\nu^{\otimes5}\bigr).
}
\tag{24}
$$
这五个输入都是同一个原 sigma 测度，没有任何秩零参考斜率，
也没有把某个 Mellin 乘积当成函数商。

令 $\Xi_{\mathrm{prim}}$ 为 (24) 限制“至少一个原输入为单位”的整个输出。
两个辅助输出仍可同时或分别非单位，不能删除。
全部五个输入在 $p$ 内时，(1) 给 $\lambda^5$，
五次权 $Y_5^5$ 给 $\kappa^5$。所以
$$
\boxed{
\Xi=\Xi_{\mathrm{prim}}+t_p^5[\kappa,\kappa]_*\Xi.
}
\tag{25}
$$
由 $v_p(t_p)=1$，(25) 给真正的范数收敛重构
$$
\boxed{
\Xi=\sum_{n\ge0}t_p^{5n}[\kappa^n,\kappa^n]_*
                     \Xi_{\mathrm{prim}},
\qquad
v_p(\text{截至 }n=M\text{ 后的尾})\ge5(M+1).
}
\tag{26}
$$
原整范数至多一，任意有界整测试都可使用这个尾界。
$\Xi_{\mathrm{prim}}$ 的整个质量准确为 $1-t_p^5$，是单位。

这份收缩与 (23) 的单位标量 $\lambda_C$ 不矛盾：
“全部五个输入在 $p$ 内”只是“两条辅助输出在 $p$ 内”的一个子域。
原单位输入之间的相加 carry 仍由 $\Xi_{\mathrm{prim}}$ 保存。
例如第一个边缘的完整 $p$ 域恰为
$$
(\operatorname{pr}_1)_*\Xi_{\mathrm{prim}}\big|_p
            =(\lambda_C-t_p^5)[\kappa]_*\rho_2.
\tag{27}
$$
$\lambda_C-t_p^5$ 是单位。第二个边缘相同。
更深的单边环带由同一 core 给
$\lambda_C^{n-1}(\lambda_C-t_p^5)[\kappa^n]_*\rho_2^\times$；
两边同时的相关 carry 则仍由 (24)–(26) 的真实二维输出读出，
本篇不把它写成两个边缘的乘积。

## 7. 第一条真实混合矩及相关性

原 sigma 在 $b=1$ 的必要三项为
$$
\sigma(z)=z+\frac{z^7}{210}
                 -\frac{z^{13}}{1801800}+\cdots.
$$
它们直接由 $x''=6x^2$、$x=z^{-2}-bz^4/7+\cdots$、
$(\log\sigma)''=-x$ 得到；一般 $b$ 的后两项分别乘 $b,b^2$。

将这些实际系数代入 (19) 的有限表达，完整聚合两辅助的六次项，得到
$$
\boxed{[v^6w^6]\Psi(v,w)=-\frac{7b^2}{65610}.}
\tag{28}
$$
证书按原六因子分别求导和相加，保留了所有平方交叉项。
总阶十八只需要上面三项，因此这里没有未截尾的误差。

另一方面
$$
C(z)=-1-\frac{3b}{10}z^6+\cdots,
\qquad
\widehat{\rho_2}(v)=-C(v/\delta)
                   =1-\frac b{90}v^6+\cdots.
$$
独立乘积的同一系数应为 $b^2/8100$，与 (28) 不同，准确差为
$$
\boxed{
[v^6w^6]\{\Psi(v,w)-\widehat{\rho_2}(v)\widehat{\rho_2}(w)\}
                     =-\frac{151b^2}{656100}\ne0.
}
\tag{29}
$$
因此全联合因子化 (22) 与两个辅助的相关性同时成立：
分离的是原输出 $Y$ 和整个辅助二元组，并非把二元组拆成两个独立变量。

原实际混合矩更直接地写为
$$
\boxed{
\int L_r^6L_s^6\,d\Xi
 =(6!)^2\Omega^{12}[v^6w^6]\Psi
 =-\frac{4480}{81}b^2\Omega^{12}.
}
\tag{30}
$$
其值对所有本篇普通 $p>7$ 都是单位。
这是一个已经完整支付的二维辅助输入，不是原 $J_S'$ 的非零断言。

(30) 还说明存在一个分别 $\mu_6$ 不变、位于双方单位域的开闭集合 $D$，
使 $\Xi(D)$ 为单位。证明是对模 $p$ 的单位余类分别作 $\mu_6$ 轨道分组：
$L_r^6L_s^6$ 在每个轨道上恒定为一个单位；
在任一辅助非单位的域上它模 $p$ 为零。
若所有这些轨道域的质量都在 $p$ 内，(30) 也在 $p$ 内，矛盾。
这只给一个实际单位域存在性，不指定它一定是某条所需碰撞线管。

## 8. 相关域也准确返回原完整中央

对任何有界连续函数 $h(L_r,L_s)$，只要它对两坐标分别的 $\mu_6$ 作用不变，
就可在未平均的原核上使用 (22)，得到
$$
\boxed{
Y_*\{h(L_r,L_s)\eta_6\}
                         =\Xi(h)\nu_S.
}
\tag{31}
$$
因此所有 tame 的完整函数和原 principal 中央导数满足
$$
\boxed{
J_{S;h,\ell}(u)=\Xi(h)J_{S,\ell}(u),\qquad
J_{S;h}'(0)=\Xi(h)J_S'(0).
}
\tag{32}
$$
没有附加的质量斜率或输出尺度项，因为 (31) 是完整输出测度的常标量等式。

本篇新支付的 $h$ 可以真正耦合两辅助坐标，例如
$$
\mathbf1_{\{
L_r,L_s\in\mathbf Z_p^\times,\ 
v_p(L_r^6-L_s^6)\ge N
\}},
\tag{33}
$$
或同时指定各自深度、环带与任意六次幂关系。
(33) 的系数是整个原 $\Xi$ 对该域的质量；
所有单位输入相加产生的非单位 carry 都由 (24)–(26) 保留。
不能只取其某一条单位相位分支而不支付其他分支。

特别 $h=L_r^6L_s^6$ 时，(30)、(32) 给一个对全部本篇普通素数都无损的
真实混合中央观察。若原 $J_S'=0$，(31) 控制的全部相关域中央导数确实都为零；
没有假定单个负五次矩非零。

## 9. 与三辅助及原叶深度条件的区别

R341 的非零交换差没有阻止 (22)，因为本篇是直接形成
$(Y,L_r,L_s)$ 的联合输出，再对其两个辅助坐标平均。
它没有交换两个在原六变量上不相互保持的投影。

本篇也没有推出任意三个重叠辅助坐标的相同分解。
两个辅助作用后的第六个 sigma 保持未移位，
是第2节的质量零与第4节全部挠点降阶的重要真实输入。
当第三条法向量覆盖第六槽时，这项条件已改变，不能套用本篇证明。

R339 的非零原叶域包含对其余原 sigma 和范数三链叶变量的额外独立深度限制。
这些限制并不都只是 (33) 或其他 $h(L_r,L_s)$。
所以 (31) 当前支付了更广的相关辅助域控制，
仍须把原叶域的完整交叠和补域接到这些真实观察，不能从域包含直接传递零。

## 10. 精确证书及来源

生产脚本 check-jzero-overlap-pair-torsion-factorization.py 与同名 JSON
核定三个原换代表、所有 CM 理想商、两条辅助 Gaussian 的逐项消失、
degree 四／五／十／三十四的真实不变空间、四个不同的角根、
原辅助五输入常数以及混合矩 (28)–(30)。
完整全权因子化由第2–4节的线丛和挠点证明，不由低阶计算外推。
没有扫描目标素数。

- [R297：原来源与 CM7 division 因式](R297-jzero-actual-cm13-mass-kernel-cm7-product-and-angular-source.md)。
- [R316：同一个原 sigma 和普通 core](R316-jzero-low-degree-original-cores-and-complete-four-factor-carry.md)。
- [R333：原六 sigma 来源](R333-six-original-sigma-inputs-and-two-quadratic-negative-moment-return.md)。
- [R339：原叶深度非零族](R339-original-normthree-depth-family-and-a-unit-negative-moment-coefficient.md)。
- [R340：原三变量恒等式与范数三链](R340-original-ternary-fourier-joint-measure-and-collision-domains.md)。
- [R341：原混合坐标、三次 core 及源交换差](R341-original-active-triple-joints-degree-three-core-and-overlap-source.md)。

