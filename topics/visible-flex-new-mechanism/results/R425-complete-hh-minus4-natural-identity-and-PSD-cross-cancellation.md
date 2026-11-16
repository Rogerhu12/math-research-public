# R425：负四 hh 的两次完整自然观察、全曲率闭式与 PSD 交叉行消失

日期：2026-11-16。**本稿消费首次新公开 Actions 的完整原日志；只新增两个必要 self 装配和两个完整自然通量观察。没有在本地执行研究，没有重做旧 pure、forcing、响应生产、秩、profile 评价或开发检查。全曲率和正字符结论由已付原式与下面的完整密度作人类推导。**

令
$$
V(k)=[h^{-6}(\log h)^0]\widehat Q_{hh}(h,k,0),\qquad
V_0=V(0),\qquad
W=[h^{-6}k^6(\log h)^0]\widehat Q_{hh}(h,k,0).
$$
两者都是原完整正规速度二次层的成本真权 $-4$ 系数。首次新观察准确给出
$$
\boxed{
\Lambda_u(V_0)=-\frac3{16}F(u),\qquad
\Lambda_u(W)=0,\qquad
F(u)=\int(u'-xu'')^4u''' .
}
\tag{1}
$$
第一式是一个**非零 universal 自然泛函**，第二式是完整自然函数恒零。它们不把 $V_0,W$ 或整个 $Q_2$ 作为成本算子置零。

由 [R422](R422-two-term-all-curvature-structure-of-the-minus4-hh-natural-function.md) 的完整两项曲率结构，
$$
\boxed{
\Lambda_u(V(k))
=-\frac3{16}(1+k^2)^2F(u)
\quad\text{对所有实际 }k\text{ 和全部实紧 }u.
}
\tag{2}
$$
对 R413/R414 已从起点构造的共同母库及其共同自然查询，(2)只落在已付 Q4 平移像。因此任一剩余的下降负四正字符，其整个 hh 对角为零；真实 PSD 随后迫整个 hk 交叉行为零。**负四 kk 全曲率行仍须独立处理。**

本次不需要为 hh 增加 R424 的 $M_{25}$ 观察。R424 是仍可独立使用的条件性一般结论；本次获得了更强的完整 Q4 身份(1)。

## 1. 自然函数与真正的 pure-zero 校正

保持原共同右 collar、真实成本 $U$、响应空间 $\mathcal R$ 及
$$
E=(\pi,\mathcal Q),\qquad
\mathcal Q(V)(u)=\frac14[x^2]_{\rm left}V(u^2,0).
$$
$\mathcal Q$ 仍是 universal 左二次 self 系数，非整个输出函数。

沿 [R352](R352-ordered-three-moment-tail-map-and-natural-total-flux-quotient.md)、
[R406](R406-complete-weight-zero-natural-fluxes-and-canonical-joint-obstruction.md)，完整自然读出为
$$
\begin{aligned}
\Lambda_u(V)
={}&\int u'''V(u^2,0)
-\frac{16}{5}\int u'''\pi V(u)\\
&-\frac{32}{15}\int u'''\mathscr G_{V,u}(\mu(u)),
\end{aligned}
\tag{3}
$$
其中
$$
\mu(u)=
\left(
\int(u'')^2,\ \int x(u'')^2,\
\int\{x^2(u'')^2+2(u')^2\}
\right).
$$
$\mathscr G$ 是原 pure 的有序 $2+2$ 真三矩尾。已付
$$
\Lambda_\cdot(\mathcal R)=0.
\tag{4}
$$

本次复用 [R210](R210-complete-weight-minus4-pure-image-and-finite-pure-closure.md) 的两个完整 pure 列。下表的 $R_i$ 采用 **R139 原 old-column 标签**；它们不是本次九列压缩后的编号。

| 原目标 | 旧 normalized / global 列 | 原 scale | 乘该 scale 的响应组合 |
|---|---|---|---|
| $V_0$ | $60/100$ | $-1/512$ | $-24R_1-56R_2-8R_3+40R_8+8R_9-14R_{12}+10R_{15}-10R_{17}$ |
| $W$ | $63/103$ | $-5/512$ | $4R_0+(12R_1-156R_2-12R_3+192R_8+36R_9-78R_{12}+23R_{15}-32R_{17})/5$ |

记两行 scale 为 $s_i$、显示响应组合为 $C_i$，并定义
$$
\widehat V_i=V_i-s_iC_i,\qquad i\in\{0,6\}.
\tag{5}
$$
旧完整 pure 收据和(4)分别给
$$
\pi\widehat V_i=0,\qquad
\Lambda_\cdot(\widehat V_i)=\Lambda_\cdot(V_i).
\tag{6}
$$
不是本次重新求 pure 像，也不是用有限 profile 测试 pure 零。

因此新观察可以准确采用
$$
\Lambda_u(V_i)
=\Omega_u(\widehat V_i)
=-4\int u'''M^{\widehat V_i}_{-2}(u,u)
=4\left[
I_{r_*}^x\{u'''M^{\widehat V_i}_{-2}(u,u)\}
\right]_{\rm left},
\tag{7}
$$
其中 $I_{r_*}^x=-J$。原 $-4$ self 因子、共同右锚和全部内部左尾均保留。

## 2. 本次确实装配了哪些尚未付的 self 项

本次没有假称 R210 已经保存了两个完整正规 mixed 根。其已付对象是 pure 列；可只读的原输入是完整 $v^{[2]},N^{[0]},N^{[2]}$ 因子与原矩阵。

原 hh 正规式为
$$
\widehat Q_{hh}
=[\gamma^2]\{
v^{[2]}-\mathcal B_{m_0}N^{[2]}
-\mathcal B_{m_2}N^{[0]}-\Gamma(m_2)\}
-\partial_h[\alpha]v^{[2]},
\tag{8}
$$
其中 $\gamma=h_s,\alpha=h_{ss}$，沿本切片 $X=\partial_h$。执行按保存几何键取系数，并保 $\partial_h\log h$ 的可能分支。

原 R78 在真实 self 对角给
$$
(\mathcal B_EN)_{-2}(u,u)
=-\frac12N(\Phi_E(u,u);u,u).
\tag{9}
$$
所以(8)的两个负势在 $M_{-2}$ 中均贡献
$+\frac12m_E N(\Phi_E(u,u);u,u)$。这些是本次必要的新外槽收缩，原 $\Phi_E(u,u)$ 左二次尾全部保留。

尤其，没有先用 R367 的完整自然 $C_A/N_2$ 消去来删除 raw self，再沿用未经相应改变的旧 pure 坐标。那会混用两个不同层的正规化。本次完整保留(8)的两势后，才作(5)。

原 $\Gamma(m_2)$ 与 $N_0$ 基准减项不含本 $h^{-6}$ 目标，原因是原完整 $m_2$ scalar 几何支撑的最低 $h$ 次数为 $-4$。执行核对了全部原状态；这是支撑证明，不是把 $N_0$ 或中间场当作紧场。

实际选取：

- 四个原 raw 根：$V_0$ 用 `v-2_2_120`、`v-2_2_207`，$W$ 用 `v-2_2_186`、`v-2_2_288`；各对真实系数为 $1,5$，后者来自原加速度正规化。
- 七个 typed 原根；九次势项使用通过相同 typed 根与 $E$ 的缓存合并，准确只执行八个必要 self 槽收缩。
- 十一个所需原因子根只访问原 $3521$ 个 atoms 中的 $464$ 个。
- 原九响应解码访问原 $933$ 个 atoms 中的 $702$ 个，未调用原响应生产入口。

上述是必要输入消费与新 self 装配的真实账目，不是完整旧研究重跑。

## 3. 唯一公开执行及冻结来源

| 项目 | 准确身份 |
|---|---|
| run | 43787923095 |
| job | 133039635185 |
| source | 3275f8b7ea0429f42d0da196699cc9a3f2a22eae |
| [公开 job](https://github.com/Rogerhu12/math-research-public/actions/runs/43787923095/job/133039635185) | completed / success |
| 新入口 | [literature_hh_minus4_natural_flux.py](../scripts/literature_hh_minus4_natural_flux.py) |
| 请求 | [request-hh-minus4-natural-flux.json](../computations/request-hh-minus4-natural-flux.json) |
| 设计 | [hh-minus4-natural-flux-design-20261116.md](../notes/hh-minus4-natural-flux-design-20261116.md) |
| workflow | [visible-hh-minus4-natural-flux.yml](../../../.github/workflows/visible-hh-minus4-natural-flux.yml) |

四个冻结文本为：

| 文本 | bytes | SHA256 |
|---|---:|---|
| 新入口 | 29380 | 774250847785de793468d67de2ee7e8ae08a1b93fd51a981cef3674f73da5112 |
| 请求 | 9954 | 13b5e3ea43bbedc78f9611cbbd521e6124e0311e9f0e8d60e9ea17b9b32f53b1 |
| 设计 | 10075 | 59623d43fb0c1a21c0aa6437beadc67a577f1880566ad7059a2fbd205cf3fc55 |
| workflow | 3887 | 3c590a1594aed130fe4feeddfd2104bd7c654b9c0eac8e569bee1badb8d154b8 |

全部 **38 个源码身份**在请求中固定，实际逐条一致。Python 3.12.14，纯标准库；没有新增符号或数值依赖。

### 3.1 原因子、旧响应与 pure 读据

完整原因子来自 run 43651096112、source
2259b57065cfad67682f4c4319885fd5334c4f76，原目录
notes/actions-43651096112-1-local_fourth_derivative_factors/。
原 gzip 为 2132064 B / SHA256
9daddeaf6ad8e7aa647df4f8084ec803625c589bfc51f595ff0d9c680ce0dd4a；
解压原式为 11864540 B / SHA256
58e450c47123fc682f665fffb2bb66829d9d37f502b7163e2875089b72f93fd3。
原 main、receipt、逐根 digest 和源码闭包按设计逐项核对。

九个完整旧响应来自 run 43654534244、source
1177f251dc3d9455adf88b585e4c0e4bd6f7e69b 的 R139 保存原式。
原 gzip 为 76352 B / SHA256
b266eebf27d001ef90fcc94f8b49b9f9984ed5d3f7a047d9b5cef5ddffd2423b；
解压原式为 427950 B / SHA256
6e19e56d879eed7f7d741957526679521f65f06b92c42b4cb29f39fb2c2276e4。

旧 R210 pure 坐标只读消费 run 43688302217、
job 132733352458、source
1b032593b46210e7a0599a224d5c2110fe1d1606 的完整原日志：
127473 B / SHA256
0cdf6ffa15b97cf926dad70b869945a782ee153dac317ec080d1b9d15c9030d6。
两列原 scale、normalized digest、精确 framing 及 retained-order 都逐项绑定；原 global $14,16$ 对应 old $15,17$，没有混用列号。

### 3.2 两次真实规则 pull

公共仓库：

- 2026-11-16T01:43:51.917644Z 开始，01:43:53.770804Z 完成；
- 从 source 3275f8b7ea0429f42d0da196699cc9a3f2a22eae 真正 pull 到 7baaf1948ceb78eff4dfb13afc397ce422f8f13e；
- 根 README blob 为 21bd547f56590b7f2dd279d0297efb289a9b2783，本题 README blob 为 d0432faff569c8e9af7ed4809847e12880976c11；
- 两份 README 的前后 hash 相同，diff 为空，规则检查通过。

私有仓库：

- 2026-11-16T01:43:56.172560Z 开始，01:43:56.648454Z 完成；
- pull 前后均为 e5e7d4886f7efb5069379eba37e8530d561b1a5d；
- 根 README blob 保持 5ba164843b1f5802184178a82d786264404873a3，本题私有 README 仍不存在；
- 规则未变，QUEUE 仍为本会话唯一进行中的条目，未发布私有正文。

随后 workflow 回到请求钉住的 **3275f8b7 source**，核对全部38源，才运行新入口一次。真实 pull 到新 head 不代表新观察擅自改用该 head。

## 4. 原输出、费用和准确的机器边界

完整原日志为 126843 B，SHA256：
ed0bc1b6349f63dcb1e7f083e0ae2b041d2d690819117a62f57b3a208b96c3a4。

原科学 COMPLETE_REPORT 的 JSON 加 LF 为 40566 B，SHA256：
b6f59dbe859c1c84fd71df07b18bd0d9fafdd3d862e1ce2bf97f1c26a91a24fb。

| 原目标 | 完整局部密度项数 | Euler 项数 | 原 outcome |
|---|---:|---:|---|
| hh_k0 | 4 | 7 | universal_functional_nonzero_by_complete_local_Euler |
| hh_k6 | 0 | 0 | universal_functional_zero_by_complete_local_Euler |

两目标都报告：

- `fully_local=true`；
- `complete_nonlocal_constant_words=[]`；
- `natural_flux_equals_raw_Omega_by_paid_universal_pure_zero=true`；
- `same_natural_function_as_original_target_by_response_annihilation=true`。

hh_k6 的整个完整左端、局部密度与 Euler 表均为 []，不存在未归约的非局部残余。hh_k0 的四项完整密度在下一节逐字写出。

原报告的
`remaining_minus4_Q2_character_or_actual_joint_resolved=false`
保持原值。源码没有研究 kk 全曲率或实际联合截面；下面关于 hh/交叉行的结论是本稿使用 R422/R413 的独立人类推论，不回写原 report。

实际科学时间为 2.254986277 秒；其中已付数据读取
1.376327887 秒，必要输入与新 self 装配
0.810166551 秒，两个新总通量映射
0.061379512 秒。峰值 RSS 为 234208 KiB。

本次新 self 装配2个、新自然目标2个、必要 self 收缩8次。旧 pure 映射、旧 forcing 编译、旧 $N_0/N_2$ producer、旧响应 producer、旧或新开发检查、旧秩研究、profile 评价均未执行。仅新局部结果使用冻结 Euler 算法作其完整泛函判定。

全部原公式与报告只在公开 job 日志及 runner 临时输出；本稿不把可重算 payload、日志或其 blob 作为仓库交付。

## 5. 四项完整密度、忠实判据与非零的人类证明

令 $p=u',r=u''$。hh_k0 的原完整密度是
$$
\boxed{
\Lambda_u(V_0)=\int\left(
\frac38p^3r^2-\frac38xp^2r^3
+\frac3{16}x^2pr^4-\frac3{80}x^3r^5
\right).
}
\tag{10}
$$
没有对单包施三矩零，也没有未列的边项。

原 mapper 先把(7)的整个 primitive 按真实有限 word 恒等式恢复，之后才取原左 collar；内部 $J$ 的常数和左多项式一直保留。只有证明整个左式全局部，才把单字原负号换成(10)。对局部五次密度 $g$，紧 $u$ 的真端 jets 给
$$
5\int g=\int u\,\operatorname{Euler}(g).
\tag{11}
$$
因此完整 Euler 字面零与完整泛函恒零等价；没有用有限样本代替 universal 判定。

为直接核对(10)，展开
$$
F=\int(p-xr)^4r'
$$
并对每个 $r^jr'$ 作一次紧 outer IBP，得到
$$
\begin{aligned}
\int p^4r'&=-4\int p^3r^2,\\
-4\int xp^3rr'&=2\int p^3r^2+6\int xp^2r^3,\\
6\int x^2p^2r^2r'&=-4\int xp^2r^3-4\int x^2pr^4,\\
-4\int x^3pr^3r'&=3\int x^2pr^4+\int x^3r^5,\\
\int x^4r^4r'&=-\frac45\int x^3r^5.
\end{aligned}
\tag{12}
$$
所以
$$
F=\int\left(
-2p^3r^2+2xp^2r^3-x^2pr^4+\frac{x^3r^5}{5}
\right),
\tag{13}
$$
准确是 [R393](R393-nine-dimensional-natural-Q4-affine-image-and-two-character-heads.md) 与
[R420](R420-complete-zero-natural-flux-of-W4-and-static-minus4-character-elimination.md) 的完整 $C^2$ 式。将(13)乘 $-3/16$ 即得(10)，证明(1)第一式。

还可直接核其 universal 非零。记 $L=p-xr,t=u'''$，则 $L'=-xt$。对
$F=\int L^4t$ 变分，三次 IBP 中
$(L^4)'=-4xL^3t$ 使两项准确相消，余
$$
\operatorname{Euler}(F)
=-4L^3u^{(4)}+12xL^2t^2 .
$$
故(10)的 Euler 精确为
$$
\boxed{
\operatorname{Euler}(g)
=\frac34(p-xr)^2
\{(p-xr)u^{(4)}-3x(u''')^2\}.
}
\tag{14}
$$
其展开有七个非零单项；最高 $u^{(4)}$ 系数
$\frac34(p-xr)^3$ 是非零自由 jet 多项式。在任一非空合法开窗口内可取紧局部 jet 扰动，因此该泛函不可能对所有实紧 $u$ 为零。

hh_k6 的完整左式已经为空，故第二式来自完整同锚零化，而非只由 Euler 消去一个非局部余式。它仍只说明 $\Lambda(W)=0$，不说明原 $W=0$。

## 6. 原完整曲率身份和有序查询

R422 已从完整 $YC/ZZ$、加速度正规化、两势及 pure/ordered 真尾证明
$$
\Lambda_\cdot(V(k))
=S^2\{\Lambda_\cdot(V_0)+k^2\Lambda_\cdot(W)\},
\qquad S=1+k^2.
\tag{15}
$$
把首次观察(1)代入即得(2)。这是所有 $k$ 的完整原式，不是两个有限曲率点的插值。

(13)是局部五次函数，所以对任意不交实紧 $u,v$，
$$
F(su+tv)=s^5F(u)+t^5F(v).
$$
因此本整个 hh 权上的有序系数准确为
$$
\boxed{
[s^3t^2]\Lambda_{su+tv}(V(k))=0 .
}
\tag{16}
$$
该式保全部合法正仿射输运，也允许辅助右包不满足偶性或母约束。它不删除尚未知 kk 层的有序读出。

## 7. 非零 universal 函数为何仍不能成为共同负四字符

采用 R413/R414 同一次构造的实际母库
$$
u_i(x)=\rho_iU_i((x-\xi_i)/w_i),\qquad w_i>0,
$$
满足
$$
q(U_i)=0,\quad D(U_i)=D_0,\quad
E_5(U_i)=E_0,\quad D_0-E_0>0,
\tag{17}
$$
以及全部原共同 $F_{\rm rat}$、十九个根及合法窗口前提。这里不在任意已冻结母库上补设共同比例。

共同映射 $J=(E,\mathcal A)$ 含所有这些 self 的正仿射闭包和所需不交有序 $3+2$ 查询。R393 的原 Q4 平移表为
$$
NF=-4D,\qquad NG=\frac43D-2E_5,\qquad
NH_4=F/2-3G .
\tag{18}
$$
在中心偶、$M_5=0$ 母上，
$$
F(U_i(\cdot-c))=-4D_0c,\qquad
(NH_4)(U_i(\cdot-c))=6(E_0-D_0)c .
\tag{19}
$$
为保实际宽度、幅度和共同仿射参数，令
$
\Xi_i(H,c)=\rho_i^5(Hw_i)^{-7}(H\xi_i+c).
$
则准确有
$
F(C_{H,c}u_i)=-4D_0\Xi_i(H,c),\qquad
(NH_4)(C_{H,c}u_i)=6(E_0-D_0)\Xi_i(H,c).
$
全部 ordered 行由局部性为零。因此 $F$ 的共同查询列在 $NH_4$ 的像中，且(17)保证分母 $6(E_0-D_0)$ 非零。若 $D_0=0$，$F$ 列本身就是零，推理仍成立。

令 $\lambda$ 是经这个 $J$ 下降、杀 $\mathcal R$、真权 $-4$ 的原实际正字符。原平移不变性给 $\lambda N=0$。仍须保 whole $E$ 的真实费用：已付
$$
E(U_{-4})=E(\mathcal R_{-4})
\tag{20}
$$
允许对任一新增自然零差选同权响应补足其 entire $E$ 坐标，响应又杀全部自然查询。这样才能把(19)中的自然像比例传给 $\lambda$，得到其对 $F$ 代表的值为零。

同理，(1)的 universal 零差先经(20)补足旧 $E$，再用 $\lambda(\mathcal R)=0$。所以
$$
\boxed{\lambda(V_0)=\lambda(W)=\lambda(V(k))=0
\quad\forall k.}
\tag{21}
$$
(21)不是由 universal 非零推出不可控，也不是从旧 $E$ 等像直接删除未知自然函数；真正使用的是完整 Q4 查询头和同一成本的响应补偿。

## 8. 完整 hh 与 hk 行消失，保留 kk 的真实剩余

R420 已付本共同商中权 $-4$ 的
$$
a(k)=0,\qquad \mu=0.
\tag{22}
$$
由 R413 的原乘子与协变，完整二次型为
$$
B_\lambda(h,k,\omega;\nu,w)
=h^{-4}\left\{
b_\lambda(k)(\nu/h)^2+
c_\lambda(k)(\nu/h)w+
d_\lambda(k)w^2
\right\},
\tag{23}
$$
其中 $\nu=h_s,w=k_s$，仍保真实水平关系
$\omega_s=k_s/(2h)$。它的矩阵逐实际状态 PSD。

在 $\omega=0$ 切片，$b_\lambda(k)$ 正是(21)读到的原 hh 系数；其余真权由 $\lambda$ 自动排除。由(21)得 $b_\lambda(k)=0$。再用(22)和原完整协变，结论传到全部合法 $(h,k,\omega)$，没有另丢 $\Gamma$ 或历史。

于是
$$
\begin{pmatrix}
0&c_\lambda(k)/2\\
c_\lambda(k)/2&d_\lambda(k)
\end{pmatrix}\succeq0.
$$
对任意实 $\nu,w$ 的非负性，或该矩阵行列式，立即迫
$$
\boxed{
b_\lambda(k)=c_\lambda(k)=0,\qquad
d_\lambda(k)\ge0
\quad\forall k .
}
\tag{24}
$$
这里的交叉消失属于**同一个原实际正字符**的 PSD 必要条件；并没有计算或宣布 universal hk 自然算子为零。

[R421](R421-all-curvature-kk-minus6-natural-identity-and-common-character-cancellation.md) 连同 R416/R419 已独立排除完整权 $-6$ 候选。当前剩余准确是负四的完整 kk 行，含原全部 $N_0,N_2,\Gamma$、水平导数及真实尾。只核一个 kk 锚值不足以关闭它。

本稿完成(1)—(2)、(16)、(21)—(24)。这消去一个 universal 非零 hh 自然函数在当前共同查询商上的正字符作用，并由 PSD 再消交叉行；没有宣称整个 $Q_2$ 为零、所有增强正字符已排尽或 actual 联合截面已经完成。
