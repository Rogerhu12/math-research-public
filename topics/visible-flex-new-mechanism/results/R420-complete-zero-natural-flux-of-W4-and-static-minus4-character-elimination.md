# R420：W4 完整自然泛函恒零与权负四静态正字符的消失

日期：2026-11-16。**本稿消费唯一一次新公开 Actions 的完整原日志，只新增一个完整自然通量观察。没有在本地执行研究、人工检查、profile 评价或旧 pure/self/rank 计算。全曲率与正字符结论是对已发表 R417 的纸面推论。**

置
$$
V_4(k)=[h^{-4}(\log h)^0]F_0(h,k,0),\qquad
W_4=[h^{-4}k^8(\log h)^0]F_0(h,k,0).
$$
指数标签不是几何状态值；$F_0$ 保原完整 $N_0$、参考势及同一右锚。首次新观察给出
$$
\boxed{\mathcal N(W_4)(u)=\Lambda_u(W_4)\equiv0
\quad\text{对每个实紧 }C^\infty\text{ profile }u.}
\tag{1}
$$
实际输出中，整个真实左端多项式与有序 word 表已经为空。不是只在有限 profile 族上取零，也没有把未处理的非局部项交给 Euler 判据。

由 [R417](R417-two-term-static-minus4-natural-image-and-one-remaining-anchor.md) 的完整两项结构，得到
$$
\boxed{
\mathcal N(V_4(k))(u)=\frac3{32}(1+k^2)^3F(u),\qquad
F(u)=\int(u'-xu'')^4u'''.
}
\tag{2}
$$
这一层的自然函数一般仍非零；新结论消去的是 $W_4$ 方向及 R413 所余正字符的最后静态锚值。对 [R413](R413-common-mother-Q4-chain-and-exact-low-layer-character-reduction.md) 的共同增强查询商，任一权 $-4$ 的下降正字符必有
$$
\boxed{a_1=0,\qquad a(k)=0\ \text{对所有 }k,\qquad\mu=0.}
\tag{3}
$$
完整 $Q_2$ 的 PSD 条件仍未由本稿消去；不据(1)—(3)宣称全部增强正字符消失或 actual 联合截面完成。

来源：[R352](R352-ordered-three-moment-tail-map-and-natural-total-flux-quotient.md)、[R393](R393-nine-dimensional-natural-Q4-affine-image-and-two-character-heads.md)、[R402](R402-complete-static-low-layer-natural-flux-with-original-potential-and-tails.md)、[R406](R406-complete-weight-zero-natural-fluxes-and-canonical-joint-obstruction.md)、R413、[R415](R415-two-anchor-negative-character-multiplier-and-complete-static-tail-cancellation.md)、[R416](R416-all-static-curvatures-have-zero-weight-minus6-natural-flux.md)、R417，以及下列首次新公开原日志。

## 1. 原函数定义与完整 pure-zero 校正

保持原共同右 collar、完整成本空间 $U$、响应空间 $\mathcal R$，以及
$$
E=(\pi,\mathcal Q),\qquad
\mathcal Q(V)(u)=\frac14[x^2]_{\rm left}V(u^2,0).
$$
$\mathcal Q$ 是左二次 self 系数，不是整个 self 输出或总通量。

自然函数沿 R352/R406 的同一规范：
$$
\begin{aligned}
\Lambda_u(V)
={}&\int u'''V(u^2,0)
-\frac{16}{5}\int u'''\pi V(u)\\
&-\frac{32}{15}\int u'''\mathscr G_{V,u}(\mu(u)),\\
\mu(u)={}&
\left(\int(u'')^2,\ \int x(u'')^2,\
\int\{x^2(u'')^2+2(u')^2\}\right).
\end{aligned}
\tag{4}
$$
$\mathscr G$ 是原 pure 输出的有序 $2+2$ 三矩尾映射，且已付
$$
\mathcal N(\mathcal R)=0.
\tag{5}
$$
只有整个 $\pi V=0$ 时，(4)后两项才同时为零。

本次复用 [R210](R210-complete-weight-minus4-pure-image-and-finite-pure-closure.md) 已付原列 $44$，保原系数尺度 $1/512$。用 **R139 原 old-column 标签**定义
$$
\begin{aligned}
\widehat W_4=W_4-\frac1{512}\bigl(
4R_0+8R_1-24R_2-R_3+36R_8+4R_9\\
{}-17R_{12}+R_{15}-5R_{17}\bigr).
\end{aligned}
\tag{6}
$$
标签 $15,17$ 不是本次压缩列位置；原 R210 对应全局位置为 $14,16$。执行按冻结的原标签及完整 mixed 根逐项读取。

原 R210 已付完整 universal pure 坐标，因此
$$
\pi\widehat W_4=0,\qquad
\mathcal N(\widehat W_4)=\mathcal N(W_4).
\tag{7}
$$
两个身份分别来自旧完整 pure 坐标和(5)，不是本次重做 pure/rank。新目标准确为
$$
\Lambda_u(W_4)=\int u'''\widehat W_4(u^2,0)
=-4\int u'''M^{\widehat W_4}_{-2}(u,u).
\tag{8}
$$
最后的 $-4$ 是原 mode/self 规范，沿用 R406 冻结 mapper。没有把未校正的单个 $M_{-2}$ 直接当自然函数。

## 2. 唯一公开执行与原输入

| 项目 | 准确身份 |
|---|---|
| run | 43784526298 |
| job | 133029071528 |
| source | ce04a915bf8d57d6b233aa329e602c6156ef7095 |
| [公开 job](https://github.com/Rogerhu12/math-research-public/actions/runs/43784526298/job/133029071528) | completed / success |
| 新入口 | [literature_static_minus4_natural_flux.py](../scripts/literature_static_minus4_natural_flux.py) |
| 请求 | [request-static-minus4-natural-flux.json](../computations/request-static-minus4-natural-flux.json) |
| 设计 | [static-minus4-natural-flux-design-20261116.md](../notes/static-minus4-natural-flux-design-20261116.md) |
| workflow | [visible-static-minus4-natural-flux.yml](../../../.github/workflows/visible-static-minus4-natural-flux.yml) |

新入口为 20,713 B，SHA256：
c734956045b19a324f76397f251385ecc2aeb8daaf8f4aaa1beb8530da859e2b。

实际请求为 7,854 B，SHA256：
7b98bbc82e9d8a2c34f6fbf41989c5f866c668c481d69e3e92a941ba7f0165c4。

冻结 workflow 为 3,878 B，SHA256：
e4a3eea6576fe067de47eb75ced9adc82558a46f485c7e1fb3c3529d830bd3a3。

只使用 Python 标准库。全部 **36 个源码身份**在实际请求中绑定且逐一匹配。其中原 R406 完整 mapper 为 42,478 B，SHA256：
be12b9338cf5558eacb4d05b43f201871fae5d4262dd330304eaa56df3c2e12f。

### 2.1 一个旧静态原根

原静态导出来自 run 43645177423、source
2f1b809c0b0abb7a26303d36940edc203815f872；原目录为 notes/actions-43645177423-1-local_fourth_quotient。

原导出 gzip 为 657,195 B / SHA256
ea8ba97319ef3fa43ff8cacc7f98b106b13280aef4641b969f5f820194aebace；
解压原式为 3,518,194 B / SHA256
d74e87790a00a246e01438c54575c3190389e3adbdefed0cec233b6ec9a664d1。

该原生产者的小主报告状态是 **output_limit**，本稿不把它改成整个旧研究成功。其已实际导出的 430 个原表达式根有独立大小/hash 和保存原式声明；本次只解码其中
$$
\texttt{L-2\_58},\qquad
(h,k,\omega,\log h)=(-4,8,0,0).
$$
真实权 $-4$ 投影前后均为 466 项，SHA256 同为
aa0d5eab9d6b73b47fa09eea5038409f41e3a74af5150cce69e20c055d1d30d2。

原 $N_0$ 已在保存的静态根中。R417 §3 已从原式证明 $\Gamma$ 没有本 $h^{-4}$ 系数；执行没有用“忽略 $\Gamma$”代替该证明，也未重建势或参考项。

### 2.2 九个旧响应与旧 pure 收据

(6)的九个完整 mixed 响应直接来自 run 43654534244、source
1177f251dc3d9455adf88b585e4c0e4bd6f7e69b 的 R139 保存原式。原 gzip 为 76,352 B / SHA256
b266eebf27d001ef90fcc94f8b49b9f9984ed5d3f7a047d9b5cef5ddffd2423b；
解压原式为 427,950 B / SHA256
6e19e56d879eed7f7d741957526679521f65f06b92c42b4cb29f39fb2c2276e4。

旧 pure 坐标从 run 43688302217、job 132733352458、source
1b032593b46210e7a0599a224d5c2110fe1d1606 的完整原 stdout 只读消费。该日志为 127,473 B / SHA256
0cdf6ffa15b97cf926dad70b869945a782ee153dac317ec080d1b9d15c9030d6。

执行按原 result、原列 44、最终科学 status 的准确 framing/hash 核对，未重建旧主报告，未执行旧 pure 或旧秩。九个响应均直接解码，未调用旧 mixed-response producer。

校正后的完整 mixed 为 **993 项**，SHA256
b18e891c749ee095d53144aaa068c47dd6045fe88903715cad2a7b019bbda18f；
全局实对角为 **110 项**，SHA256
333c4f1d09d346cfa15eb2c39e5d66ed30bee7fe73d0473aa8abaf3b76e270cd。

## 3. 两次实际规则 pull 与执行边界

执行前公共仓库的真实 pull：

- 起点为 ce04a915bf8d57d6b233aa329e602c6156ef7095。
- 开始于 2026-11-16T01:09:16.652040Z，完成于 2026-11-16T01:09:18.972099Z。
- 实际到达 1a757004b7ebff1f43563bd57b5d13961648d681，返回码 0。
- 根 README blob 保持 21bd547f56590b7f2dd279d0297efb289a9b2783。
- 本题 README blob 保持 d0432faff569c8e9af7ed4809847e12880976c11。
- 两份 README 的 source/pull 后 hash 均匹配，diff 均为空，规则检查通过。

随后私有仓库的真实 pull：

- 开始于 2026-11-16T01:09:21.159310Z，完成于 2026-11-16T01:09:21.549406Z。
- 起点与终点均为 210d6ba3f178eefff06b6716a4e8bf55d081221c。
- 私有根 README blob 为 5ba164843b1f5802184178a82d786264404873a3；本题私有 README 不存在，保持原状态。
- 前次记录至本次、本次 pull 前后均无规则变化；QUEUE 唯一且仍为本会话进行中。
- 原日志没有发布私有正文。

规则消费后，workflow **回到请求钉住的 ce04a915 source**，核对 36 源，再且仅再运行一次新入口。公共 pull 到更新 head，不等于研究擅自使用该更新 head。

本次没有新开发检查或旧开发检查执行。旧 pure/self/Euler/rank、旧 forcing、旧响应生产、旧 $N_0/N_2$ 研究收缩、profile 评价计数均为零；必要输入只解码一静态根及九响应根。

## 4. 完整零的证据与数学含义

同一右锚的有号 primitive 为
$$
I_{r_*}^x f=\int_{r_*}^x f=-Jf.
$$
新 mapper 先恢复(8)的整个 primitive，再使用原有限 word/分部积分等式；只在取真实左 collar 时使用 **outer** 紧 profile 的平端 jets。内层 $J$ 的常数及左多项式不能据此删掉。

| 完整对象 | 项数 / 结果 |
|---|---:|
| 整个新 primitive 的 word 表 | 84 |
| 真实左端多项式与全部有序 word 表 | 0，即空表 |
| 完整局部密度 | 0，即空表 |
| 完整非局部常数 word | 0，即空表 |
| 完整 Euler 多项式 | 0，即空表 |
| profile 评价 | 0 |
| cycle fallback | 0 |

新原 primitive 的 SHA256：
a37edc12b45ac2d202f3e2b1b79e35525d43b2568c10dc782def019043a671fb。

其完整 word 表 SHA256：
f01ffbdbe5e2c6e759dcdfd1a5f628454b8825d4b353f6a6fca897cc7e41e576。

四个空表的 canonical JSON SHA256 均为
4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945。

实际 outcome 标签为 universal_functional_zero_by_complete_local_Euler；这里无需使用“非零 normal form 是否忠实”的逆向判据：**整个左端原式表先已为空**。所用 primitive、shuffle、IBP 都是同锚完整等式，故直接证明(8)对任意实紧 $u$ 为零，再由(7)得到(1)。

执行未改右锚，未丢旧 $N_0$、$\Gamma$ 或左常数。没有任何未归约非局部余项，也没有从 finite-N、有限平端多项式或数值 profile 推 universal 零。

新 mapper 统计为：195 次 primitive、129 次 fixed-color IBP、129 次 unique-high-jet IBP、217 次严格下降核对、5 次全深度 shuffle；最大 word 长度 2，cache 峰 692。它们属于本次一个新通量，不是旧研究重复。

### 4.1 费用与原日志身份

| 项目 | 秒数 |
|---|---:|
| 只读旧 pure 日志及收据 | 0.896866212 |
| 必要旧 mixed 输入解码 | 0.273982093 |
| 一个新完整 $\Omega$ 观察 | 0.188732182 |
| 科学入口总计，含其余框架开销 | 1.370958935 |

峰值 RSS 为 **94,920 KiB**。总计不把 checkout、规则 pull 和 runner 设置时间冒作研究 CPU，也未隐去必要输入恢复。

完整原 stdout 为 **103,968 B**，SHA256：
4331825126c9b3f2c7ba129437a712b5c00455d7abab9789d9a0290b9aaa1054。

完整科学 COMPLETE_REPORT JSON 加一个 LF 为 **23,562 B**，SHA256：
807ed8f2e6e9b62dbd2099617422d29845f9e2c277cff4f7affb2b470785bec0。

原 stdout 包含完整请求、两次实际 pull、全部源身份、输入核对与完整科学报告。报告保留 a1_or_remaining_Q2_character_resolved=false 和 actual_joint_control_claimed=false。本稿没有改写它们；下一节的 $a_1=0$ 是观察完成后用 R417 作出的人工数学推论。remaining $Q_2$ 与 actual joint 仍未付。

原计算输出只消费公开日志，不作为重算 payload 加入正文或 Git 文件。

## 5. 全曲率静态自然函数的闭式

R417 已在完整 self、pure、有序 $2+2$ 和 $N_0$ 响应层证明
$$
\mathcal N(V_4(k))
=(1+k^2)^3\{\mathcal N(V_4(0))+k^2\mathcal N(W_4)\}.
\tag{9}
$$
R402 的完整原尾计算已付
$$
\mathcal N(V_4(0))=\frac3{32}F.
\tag{10}
$$
代入(1)即证明(2)。

为明确完整局部性，写 $p=u',r=u''$。展开四次方，再对 $r',rr',r^2r',r^3r',r^4r'$ 分别作紧 outer 分部积分，得到
$$
\boxed{
F(u)=\int\left(
-2p^3r^2+2xp^2r^3-x^2pr^4+\frac{x^3r^5}{5}
\right).
}
\tag{11}
$$
所有边项由真平端支付，不需额外 moment-zero 假设。这与 R393 的完整 $C^2$ 五次呈示一致。因此(2)是完整自然函数的局部 $C^2$ 身份，不是第三导数平方 principal。

任意不交实紧 $u,v$ 满
$$
F(su+tv)=s^5F(u)+t^5F(v).
$$
所以本静态权的所有有序查询准确为零：
$$
\boxed{
[s^3t^2]\mathcal N(V_4(k))(su+tv)=0.
}
\tag{12}
$$
所有合法正仿射输运也保此式；不能将它推广到尚未求值的整个 $Q_2$。

## 6. 最后静态锚值的消失

取 R413/R415 的同一共同增强映射 $J=(E,\mathcal A)$，其中 $\mathcal A$ 包含实际母库及所需有序 $3+2$ 的共同正仿射闭包。母库满足那里从起点支付的条件；不在已冻结的任意母库上补设共同 $D:E_5$ 比例。

设 $\lambda$ 是经 $J$ 下降、杀 $\mathcal R$、真权 $-4$ 的原实际正字符。旧已付
$$
E(U_{-4})=E(\mathcal R_{-4}).
\tag{13}
$$
(1)给 $\mathcal A(W_4)=0$。由(13)取同权真实响应 $R_*$ 使 $E(W_4)=E(R_*)$。响应的自然查询也零，所以 $J(W_4)=J(R_*)$，从而
$$
\lambda(W_4)=\lambda(R_*)=0.
\tag{14}
$$
这是“完整新增自然核 + 旧 $E$ 等像”的联合推理；**没有只用旧 $E$ 等像杀未知自然值**。

R417 已付
$$
a(k)=\frac{a_1}{8}k^2(1+k^2)^3,\qquad
\lambda(W_4)=a_1/8,\qquad \mu=2a_1p_2^*.
\tag{15}
$$
代入(14)即得(3)。按原完整协变，所有实际状态上
$$
\boxed{
\lambda F_0(h,k,\omega)=0,\qquad
\lambda F_0-\mu m_0=0.
}
\tag{16}
$$
这是下降正字符对完整静态层的值，不是把 $F_0$ 作为 $U$ 元素置零，也不否定(2)的非零自然函数。

R416 已独立清掉权 $-6$ 的完整静态函数和乘子。至此，R413 两个剩余候选负权都没有静态标量或八矩乘子余量。若它们仍非零，只能通过原完整速度二次型表现。

## 7. 剩余门

原二次正规式仍须按
$$
\widehat Q_2=\operatorname{IBP}\left(
v_2-\mathcal B_{m_0}N_2-\mathcal B_{m_2}N_0
\right)-\Gamma(m_2)
\tag{17}
$$
处理，保同一右锚、全部历史、势及参考态。$\mu=0$ 不授权删除其中任何一项。

权 $-4$ 现在只余逐实际 $k$ 的真实对称矩阵
$$
\begin{pmatrix}
b_\lambda(k)&c_\lambda(k)/2\\
c_\lambda(k)/2&d_\lambda(k)
\end{pmatrix}\succeq0.
\tag{18}
$$
本稿未新求三个完整系数，也未从静态 universal 零外推动态层。它没有增加母包观察或重做十九根，不授 whole $E$、全部有限自然读出、内部通量和同一二阶规范的最终 actual 联合目标。

已完成的新结论是：(1)整个 $W_4$ 自然泛函恒零；(2)(11)(12)本静态权的完整函数及有序零式；(3)(16)共同增强权负四正字符的静态锚值与唯一乘子消失。
