# R625 高度内移的真实新输入：既有协变的应用与原完整方程接线

会话 `Astra-new-mechanism-1f4a61a4-20261127`，2026-11-27。
**具体新输入与源码范围；未在本地执行科学，也未宣称新候选已合法或有根。**
这不是新登记一遍齐次定理：高度/字符协变、全八矩权重及原历史算子的处理已经见
[R89](../results/R89-affine-covariance-and-positive-multiple-pair-P1.md)、
[R120](../results/R120-G-lineality-of-the-closed-fourth-cost-cone.md)、
[R322](../results/R322-full-self-scaling-shift-and-exact-reduction-to-the-matching-response-weight.md)。
本文只把这些已付身份应用于[刚完成的实际 dense 终态](2026-11-27-r625-dense-feasible-natural-final-agent.md)，给出原母不变时最短、可计费的真实后继输入。

## 1. 实际换输入的依据和准确来源

原run45916412405/job140236602211，source `5033f5164ae46452a990ef0d9c68b249b6cb358c`，已经完成33份全行QR/SVD和56份完整阻尼解、10次接受。实际112份新C²曲线被原物理盒拒，最后接受态的fine又触发同一原物理盒；其fine是**pending、未合格**。

原ODE max `43092719966557.664`、原merit `143740573404817.38`；最后完整coarse实际ruling `34113723869318.57`、真末max `.2672745520455645`。原存储末十行0没有代付任何一条真history。Coarse实际hmax `2.9999999999999996`，原存储末h `2.9999999999920437`；这里有明确内移依据，但原generic盒异常没有逐lane记录，不能据此把全部失败都归因于h。

新输入必须来自这次最后接受的65×19状态，而非退回更早的有fine态：

- 原stdout1368216 B，SHA256 `2d5f7e7e6738a25b6c92b68a5e5ed40f20b03d50614c1a9b5c3c0a53e4bcff0c`。
- 原唯一FINAL逐字JSON204563 B，SHA256 `7ccc74db2edde1e562eea0e9d3279b2372d4c3cf37db40da5eda244cf35963ea`。
- 原完整payload26408 B，SHA256 `34927f117d04fc3c80cb27f199f169acb5c5fb60f65a54b60d692b8fd7525b5a`，键序仍 `parameters,x,original_nineteen_states,coordinate_order,fixed_gauge_unit,fixed_gauge_anchor_LD_decimal`。
- 原前三键checkpoint26122 B，SHA256 `b0865ddb8e5cc8bf45006893dfd9e47e0a1c7a42c600839ed66282e9536adc99`。
- 原参数202 B，SHA256 `05d2ad66305ac2432072cbad69541b2d0c9b97dffa8c0d0cecde4f936e992112`。

后继启动器只一次消费该原stdout。完整raw字节身份不替换成pretty JSON文件的字节身份。旧候选不被追授连续合法性；旧失败、部分积分和全部成本原样继承。

## 2. 已有高度协变在本输入中的准确含义

固定物理s和L，取常数

$$a=9/10,\qquad h_a=ah,\qquad k_a=k.$$

旧几何曲线由实际65节点位置/速度及共用二阶导数的quintic Hermite `ActualC2StateCurve` 定义。源码的高度二阶导数先由gamma节点的三次样条求得，并在中心替为a0；这一构造对全部高度输入线性。因此同时缩放h节点、gamma节点、中心H和a0，就在精确算术下给整条同一C²曲线 $h_a=ah$，不只缩放观察点。k全部输入不变。

原水平式与原密度记号沿用[R609](../results/R609-true-integral-histories-and-kinetic-input.md)：

$$
\eta=\int_0^s\frac{k_t}{2h}\,dt,\quad d=h\eta-k,\quad
d_s=\gamma\eta-\upsilon/2,\quad q=1+d^2,
$$
$$
c_1=2k\eta-(k^2+1)/h,\quad
c_0=k\eta^2-(k^2+1)\eta/h,\quad C=\gamma q/h-2d d_s.
$$

直接应用已付协变：

$$
\gamma_a=a\gamma,\quad \upsilon_a=\upsilon,\quad
\eta_a=\eta/a,\quad d_a=d,\quad(d_s)_a=d_s,\quad q_a=q,
$$
$$
(c_1)_a=c_1/a,\quad(c_0)_a=c_0/a^2,\quad C_a=C.
$$

八槽顺序固定为 $(p_0,p_1,p_2,t_1,r_1,s_1,s_0,r_0)$；其密度及真实累计历史权重为

$$
M_a=\operatorname{diag}(a^{-1},1,a,1,a^{-2},a^{-1},a^{-2},a^{-3})M,
$$
$$
A_a=\operatorname{diag}(a^{-1},1,a,1,a^{-2},a^{-1},a^{-2},a^{-3})A,
$$

第二式要求原中心历史也按同权重变换，并且A确为原积分解。四个自由中心 $(p_{0c},p_{2c},s_{1c},r_{0c})$ 在新输入中正按 $(a^{-1},a,a^{-1},a^{-3})$ 变换；四个偶中心仍0。

这不授权把旧独立存储A数组直接当真A。旧状态有大真/存历史差；新源从改变后的实际C²曲线重新积分eta和全部M，只把这份真实积分写入新初始history。四自由中心选择不改成别的尾积分重选，全部新非零真末A保留，交给原末十行继续求解。

原两个几何积分身份也同时保留：

$$h_a(s)-aH=a\int_0^s\gamma(t)\,dt.$$

原frame仅由k驱动，k不变时同初frame不变；原中心线满足 $\alpha_s=h^2T$，因此同初位置下

$$\alpha_a(s)-\alpha_a(0)=a^2\{\alpha(s)-\alpha(0)\}.$$

这只是输入变换；没有据此支付末pose或宏观几何门，也没有偷偷改原物理s或L。

## 3. 四个真实偶端组合全都不变

由上述权重，R609原四行

$$
\left(\frac{A_{p_1}(L)}L,\frac{8A_{t_1}(L)+2A_{p_1}(L)}L,
\frac{8H^2A_{r_1}(L)}L,\frac{4H^2A_{s_0}(L)}L\right)
$$

在精确高度协变下**全部不变**，不是仅动能一行不变。来源最后coarse实际四行为

```text
[.12727359620944861,-.725919243928372,
 -.8460404746253527,.008915526469788434]
```

新输入会同次重报完整真积分；浮点求积/重建差异不得冒数学改善。特别原准确身份

$$8A_{t_1}(L)+2A_{p_1}(L)=\int_0^L\{k^2-1-(h_s/h)^2\}\,ds$$

不因h同比缩小变好。此次新输入针对当前物理壁及其可行方向；真实偶端、原两ruling和所有原ODE仍由后继求解支付。没有把旧三角兼容输入的首层等式、R626/R627尾条件或旧已合格fine移给当前状态。

## 4. 中心图、规范和物理盒：哪些保留，哪些重算

中心 $v=k_s(0)$ 不变，$a_0=h_{ss}(0)$ 乘a；因此

$$d_s(0)=-v/2,\qquad \beta_{ss}(0)=a_0-Hv^2/4$$

分别不变和乘a。来源报告 $v=-.5375978991126716$、$\beta_{ss}(0)=.36774497212243634$；纸面变换保负v支，并使中心正beta仍远离原保护下限.05。源码仍按原完整式实评，不用这些浮点读数替连续根证明。

更一般，完整规范系数

$$\beta(s)=\frac{h^2-H^2(1+d^2)}{2h}$$

乘a；权向量 $w=(q/(4h),d/2,h/4)$ 的三槽分别乘 $(a^{-1},1,a)$。

原LD锚和单位原样读入：

```text
unit=3967798143562589
anchor=[-1.037280766893158508211784e+00,
         7.782682886905499593734741e+12,
         6.374197522561954399871826e+13]
```

两个自由offset u1/u2保持原值，所以两全程常数 $\zeta_1,\zeta_2$ 的原物理值保持。**$\zeta_0$ 重新由新中心的完整原R0/Ch/a0身份计算**，保全部有限epsilon系数。这是最短的单高度新初猜，没有再增加一次实际j/f到两规范的重拟合。

实际新C²的中心j不变、f乘a（精确算术），但保持两自由规范后，原反馈隐式要求的高阶中心jets可能不同。初猜不宣称两者相等或中心R1/R2已付；全原19flow与真实ruling读数会直接保留这个缺口。混合规范图仍是已付的原三角图局部等价坐标，完整10参数Jet、29维原feedback、左端链及长度链不变。

还须区分 $\zeta$ 与原物理 $\nu$：

$$\bar\nu=(\zeta_0-H^2\zeta_2,\zeta_1,\zeta_2),\quad
\nu=\bar\nu-2r_c,\quad\widehat\nu=\bar\nu-2E_c.$$

H、中心rc/Ec及zeta0都改变，不能声称整条原nu不变。实际完整新读数重报它们。

如果某条旧实际连续曲线已有 $m\le h\le M$、$|\gamma|\le G$、$|\eta|\le E$，高度内移能保原盒的准确条件是

$$am>4/5,\quad aM<3,\quad aG<6,\quad E/a<1,$$

连同未变k/upsilon/L以及 $a\beta_{ss}(0)>.05$。当前旧fine失败，所以不把旧coarse范围当成这些连续假设。新输入按原门实评；尤其eta放大为原值的1/a，不能因h上界内移而省去eta、k或两速度的原检查。

## 5. 固定母时不能搬运旧rho、正势或ruling

R89完整曲面协变还会同时变换字符坐标、profile、右锚和全部原算子。当前有限epsilon母固定在原窗口[4,6]，18块/576微包/右锚不移动，因此此次只应用真实运动学/八矩权重，**不应用整曲面ruling不变的结论**。

例如profile上的 $Q(y)=1+(hy+d)^2$ 变成 $Q(ay)$；在固定的实际母节点和profile上这不是原Q。既有leading身份 $C_{A_a}(y)=a^{-3}C_A(ay)$、$V_a(y)=a^{-3}V(ay)$ 也只说明采样位置变了，不能把固定母上的正平方势简化成一个常数倍率，更不能省略有限宽度余项。

新原六rho一律按同一完整函数重积分：

$$
(\rho_j^+)_s=\frac{C_j^0(g_a,A_a)+h_{a,ss}C_j^h(g_a,A_a)+k_{ss}C_j^k(g_a,A_a)}{q^2},
$$
$$
(\rho_j^-)_s=-\frac{C_j^0(g_a^-,JA_a)+h_{a,ss}C_j^h(g_a^-,JA_a)-k_{ss}C_j^k(g_a^-,JA_a)}{q^2}.
$$

各中心rho仍0，负侧最外负号作用全部项。完整正势系数仍1、原不截断Gram仍用原母；新中心rc/Ec、全程势差、原两ruling全部重新评价。不存在本范围已证明的简单rho齐次权重。

旧全状态中未满足原ODE的独立history节点不被同次放大后当作新真实数据。新19初态的h/k/gamma/upsilon保明确缩放后的插值输入；eta、8A、6rho仅取新曲线同次真积分。真末值非零就如实保留，原19/末10求解器处理它们。

## 6. 为什么这次没有顺手加k动能投影

R609§4末已经给固定h、$k\mapsto\lambda k$ 时准确动能投影，旧严格合法正能量输入在那里仅需要 $0<\lambda<1$，故可继承原盒。这条结论不重复登记。

一般令 $K=\int k^2ds>0$、$G=\int(h_s/h)^2ds$，原单行准确根为

$$\lambda_*^2=(L+G)/K.$$

若原动能组合为负，所需lambda大于1。新组合高度a和曲率lambda还会给

$$\eta_{a,\lambda}=\lambda\eta/a,\qquad v_\lambda=\lambda v,\qquad
\beta_{ss,a,\lambda}(0)=a\{a_0-H\lambda^2v^2/4\}.$$

因此除原k、upsilon、eta盒外，还必须有

$$\lambda^2<\frac{4(a_0-.05/a)}{Hv^2}$$

才保当前正beta保护图。来源只保存动能组合，没有保存独立K、G；这里不从未存积分猜lambda，也不另开一次投影探针。当前范围明确 **lambda=1**。真实四偶缺口保持，由新输入之后的完整求解处理。

## 7. 新源的执行次序与不重复已付工作

新源 `scripts/r625_homothetic_true_input_continuation_agent.py` 导入已冻结的完整行dense类，QR/SVD、全部原行和Euclidean惩罚不变。只变如下真实入口：

1. 一次读原自然终态stdout，核原literal FINAL、原state/参数、十次接受与fine pending身份；保存旧源和全部成本。
2. 恢复原已存LD锚；必要未存原系数表/正Gram按原定义重建，全部计费。无旧D/root/解析seed、旧母资格、旧中心图或旧fine重跑。
3. 在LD中用十进制a=.9形成新高度/中心量，再写入原binary64配点坐标。精确纸面身份与浮点存储不混同。k、L、u1/u2不动，四自由中心按已付权重变换。
4. 评价一次完整新mixed中心图；据新h/k建立实际C²，按原32panel/Gauss16/65观察重新积分eta/8A/6rho、完整正势和两ruling。任何原物理盒失败直接保失败与部分成本。
5. 用这同一次实际积分填新初始history；保原非零真末。没有第二次初始真积分。一个临时只读capture保存原FullHistory已计算的curve/data，读取LD对binary64写回误差后释放，不添加系数或积分调用。
6. 新中心完整Jet由单次cache交给第一次必要原flow评价，免同参数重复中心计算。准备好的实际readout只在参数和h/k/gamma/upsilon插值输入逐字相同时复用；这是同对象身份核对，不是新的科学资格门。
7. 从此用原完整19/末10 BVP、同一dense方向/接受算法继续；每一真实新接受态重新付实际曲线积分。只有原配点+stored端联合门过后才允许原129点第二网格。

新trust明确设.25，来源耗尽trust `3.725290298461914e-9` 保历史；初damping沿实际末 **`.00025811747917131974`**。新曲线和真实history已经不同，这不是只给原停滞态重设半径或声称恢复旧内存后端。

初始fixed fine一律pending。末fixed fine仍在原时间预算下对同一真实候选执行，失败或余量不足如实pending；来源未合格fine没有被转换为资格。没有增加旧source不支持的算法分支或额外计算探针。

## 8. 保留的原门、费用与输出范围

同一R598有限epsilon=1/12000母、全部负侧符号和单条路径的常规范、完整正势系数1、原物理盒、四自由中心及全十末行全部保持。原ODE1e-7、stored/true末1e-8、实际ruling1e-7、同节点真history1e-7均未降低。局部feedback代数相消的LD地板不能用归一化残差遮盖。

所有实际中心图、new-seed真shape/eta/M/rho/ruling、原flow/Jac、全部模式QR/SVD和每lambda解、失败试步与失败fine都进入同一公开科学时钟。原3300秒/180末预留/3120普通边界不变；新增准备在每个必要阶段前后check，ClockCheckpoint保最后可用状态及完整已耗时间。旧stdout准备在无科学的父启动器中另列秒数，科学子进程无凭据。

源完整保原11段费用链，新增这一段不清零旧成本。新输入完成但原flow尚未完成时，FINAL仍保存这份新真实history初态并明确origin；若新输入本身失败，则保原未合格源、失败stage和部分成本，不能冒已生成合法新态。之后每次接受按原完整payload身份保存。

stdout包含必要状态、报告和小型factor收据；不保存/提交原数组文件、artifact、release，不改git或其他仓库。此范围只产生新的实际输入及原求解证据；连续误差、原精确根、pose/reach和本课题完成标准仍须另由真实成功支付。
