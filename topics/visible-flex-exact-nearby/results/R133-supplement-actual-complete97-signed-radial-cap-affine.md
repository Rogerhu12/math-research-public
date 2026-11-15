# R133 补篇：actual 完整 97 列径向相减 signed affine 与两帽域误差

2026-11-15，visible-exact / tail_connector；简称 **SCA**。

**唯一 SC3 公开运行已经成功并冻结。** Run **43754452928/1** 的科学 child
返回 0，20 个完整门全部通过；32 组、7908 个原 scalar quarters、
4 个原 pilot、完整 128 个物理测试模和全部 97 个输入均已消费。
本篇只读原成功小结论，记录新 signed functional 和其完整误差；
没有重新执行 QR、原 enclosure、旧 Gram、RW、Green 或成功 SC 算术。

最先区分两个已经得到的量：完整已知参数模型的统一上界约为
$3.8444\,10^{-13}$；将原未知修正、非线性、左缺陷和外端误差全加回后，
目前完整 affine97 上界约为 $1.61721\,10^{-7}$。
后者才是同一真实帽图的完整边界源上界。小的已知模型不替代该误差，
本运行没有宣称 low trace、core 自映像、完整 BVP 逆或全局曲面通过。

## 1. 三个完整 actual 原件与冻结身份

| 原件 | Git blob | bytes | SHA256 |
|---|---|---:|---|
| [完整科学结论](../notes/signed_cap_affine_functional_ci/run-43754452928-1/actual-scientific-conclusion.json) | a05d881b0b160299d39cb522ee88304a45b20af0 | 23672 | f0838341d4f661714328da407c9a45f7ef137c43e8ab1ca7f4adfc2b12e7893c |
| [完整执行记录](../notes/signed_cap_affine_functional_ci/run-43754452928-1/execution.json) | 34050b25b7197fb27d886b40c8f3366726e34f08 | 43738 | 9ce9955fade952563c6d2dc2ca7650b43a3752d3b10e9051a798ffd73fe2c5e9 |
| [实际简报](../notes/signed_cap_affine_functional_ci/run-43754452928-1/actual-result.md) | 625a4cbfb1f00f6b41f511556bb9b2c6815a1618 | 8796 | aded5e9a2c65a9033f379ec7ed315091df0d0be4f27819949124c84037ecbde3 |

唯一 head 为 `555d311ba50ab79bce0dade4f168053d0d7bc0e9`，
workflow 为 `.github/workflows/visible-exact-signed-cap-affine-functional.yml`，
job **132935365422**。Actions 记录创建于 19:48:15 UTC，最终
23:30:02 UTC 更新为 `completed/success`；12 个实际 job steps 全部 success。
执行记录的科学阶段从 19:48:44.019464 UTC 开始，
23:29:52.737741 UTC 完成。child wall 为原记录
`13195.092762536` 秒；科学自身计时为 `13194.739746157` 秒。
这两个字段分别属于 wrapper 和科学子进程，不互相覆盖。

科学运行时为 Python 3.12.14、python-flint 0.9.0、NumPy 2.3.5、
256 bits。实际 source、helper、reader、worker 分别如下。

| 文件 | Git blob | bytes | SHA256 |
|---|---|---:|---|
| [SCI](../scripts/fourfold_codazzi_signed_cap_affine_functional.py) | a3e2150166472fd5c08b5508cd30dda12be7836f | 44167 | 41b8f50cd7faafc438f37f3f4514caa24142af63d9921044d91ead67d6fcd1dd |
| [完整矩 helper](../scripts/fourfold_codazzi_signed_cap_radial_moments.py) | 830b03d7f1519900805e3458265a974f12183e6e | 17314 | 6f868fafd82a62c7c7a3a04bebbb0da1363209c80097f218f086781d37f2efb4 |
| [原件 reader](../scripts/fourfold_codazzi_signed_cap_original_inputs.py) | 91441d2be8a8066130eb5f8a4eb59df46964300b | 14299 | a7c099608ec6ef1504a1d30b9cabbe9232bdd1dfd0390e28bbfd9fc836772ad0 |
| [public worker](../scripts/fourfold_codazzi_signed_cap_affine_functional_ci.py) | eb2b1c99c31ffe339cdb7eeb6333684cee884229 | 59315 | 414e55cb40c516ad02cbba8ae45ac4772f18545dbbfaab8adae5f2ef2abcf6ce |

[实际 manifest](../notes/2026-11-15-R133-signed-cap-affine-functional-CI-inputs.json)
为 38760 B，SHA256
`cd28e23a13ef68281dd4813de793896e89b235926936d2668e64e7bfe6e22aa9`；
workflow 为 4468 B，SHA256
`6936992edd5c5a5fdaf28e4513c14321ed5a978e1a58c1f9838159ef5d488e5e`。
合同是已发布 [SC](R133-supplement-exact-radial-subtraction-and-complete-known-cap-affine-moments.md)，
blob `0e2fcd353d8c6c2274633d7e052f645f0d9bf534`，
20669 B，SHA256
`927c3ba2ada01e1a571ce4d180c7d1e41ac25b1dda273cc6aef90511d40b9583`。
它调用 [SA 的完整物理伴随式及第 7a 节左端重排](R133-supplement-signed-physical-cap-affine-and-complete-adjoint-receivers.md)，
最终 SA SHA256 为
`85e07aba2d895c160be6c307da9ff0740fb817bbad6f3813d0acf3242e0f35d1`。

## 2. 同一对象、两种帽输入域与完整均值

本次固定原 $\eta_0,\nu$ 与 exact repaired ac1/440866 中心，
真实物理帽是
$$
 [L,R]=[9/10,25/8],\qquad |\delta|\le d=10^{-10}.
 \tag{SCA.1}
$$
原完整 source 参数保留
$$
 \alpha=\frac{6890507429876859}{9007199254740992},\quad
 \eta_0=-\frac{7789843107295549}{4611686018427387904},\quad
 \nu=-\frac{2572625729470897}{72057594037927936}.
 \tag{SCA.2}
$$
中心的原 $\alpha$ 只乘一次；canonical response $Z_{\rm can}$
是完整 raw193 moving 方向，不再乘 $\alpha$。
所有物理角频率为 $4j$，圆测度归一；体积分用普通 $dr$。
原两个 physical mean 不能因 odd/even 或 phase 变换而删去。

令 $\widehat W=\Psi(\widehat Q)$，
$W_\delta=\Psi(\widehat Q+\delta Z_{\rm can})$，
$W_*^f$ 是原 M 真实帽图在相应输入上的同一个态。
未知量仍是
$$
 y=W_*^f-\widehat W,\qquad
 \rho=3\,10^{-6},\qquad
 \zeta_R=9.9\,10^{-10},\qquad
 \|f_B\|\le2^{-60}.
 \tag{SCA.3}
$$
这里 $\|f_B\|$、固定 height 单位、反射规范和独立均值均沿原
[完整 M product](R133-supplement-two-input-zero-width-cap-Phi-and-complete-inner-ports.md)。
新 radial subtraction 只改变已知量的计算方式，不缩小 $y$ 的 prior，
不把原完整非零 affine 基点换为零。

本次分别保存两行：原完整 $\|\gamma\|_{\mathcal A_0}\le10^{-9}$ 帽域，
以及 $\|\gamma\|_{\mathcal A_0}\le10^{-9}/128$ 的子域。
两行均要求实际物理非均值输入就是 SC.7 所需的 selected $C$ trace；
没有由其中一行自动授予其他输入或未知同态匹配。
在后续 [SR](R133-supplement-uniform-secant-cap-rows-and-complete-finite193-nonlinear-receivers.md)
及已发布的 value/difference receiver 链中，known affine 可以用其实际所属的小域，
但未知 secant 段仍须单独属于所消费的 CPA case。本实际小结不修改原 receiver 定理。

## 3. 本次真正计算的 signed functional

精确径向参考 $W_{\rm ref}=(0,1/s)$ 满足与 $\widehat W$ 相同的
intrinsic 物理方程。令 $U=\widehat W-W_{\rm ref}$。
SC.7 将全部已知体源、两端和 selected 左项同时重写为
$$
 \begin{split}
 \widetilde{\mathcal B}_{\lambda,\delta}^{\,f}
 ={}&\langle z_\lambda(R),U(R)\rangle
   -\langle z_\lambda(L),W_\delta(L)-W_{\rm ref}(L)\rangle\\
 &-\sum_\tau\langle[z_\lambda]_\tau,U(\tau)\rangle
   +\int_L^R\mathcal G_\lambda\,dr\\
 &-\langle Jz_{\lambda,B}(R),r_D^f\rangle
   -z_{\lambda,C,0}(R)r_m^f .
 \end{split}
 \tag{SCA.4}
$$
$z_\lambda$ 是原 128 odd、128 even 加完整 even mean 的同一 Hermite 伴随试件，
$\lambda$ 有完整 97 个正交输入。
所有共享节点的试件值已实际逐值相等，所以本对象的内部 $[z]$ 精确为零；
这不声称所有导数连续，也不把其他实际 PDE 的接缝跳项删掉。
真 $L=9/10$ 使用原首 Hermite 片的准确短延拓。

最后两项的 signed 数值本次没有计算；它们保留为完整 A.15 缺项费。
其余已知项给三组完整 signed97 coefficients $a_0,a_1,a_2$ 和
统一余量 $\varepsilon_3$：
$$
 \widehat b_\delta=a_0+\delta a_1+\delta^2a_2+r_3(\delta),
 \qquad \|r_3(\delta)\|_{97}\le\varepsilon_3 .
 \tag{SCA.5}
$$
$\widehat b_\delta$ 是已知试件配对的包围，不是已经求得的未知 exact cap correction。

科学文件的
`complete_signed97_parameter_model.coefficients_in_increasing_delta_power`
逐字保存全部 $3\times97$ 球；第 96 个零基索引是独立 scalar mean 输入。
非均值 sine/cosine pairing 权为 $1/2$，mean 权为 $1$。
没有截掉均值、以一个 norm 代替 signed 向量，或额外乘 $\sqrt{97}$。

## 4. 完整覆盖和真实径向积分

实际覆盖为 32 组、7908 quarters、7908 公共交段、
31 个相邻 slice joins。四个原 pilot 的 quarter 索引是
$0,64,4096,7907$，本次全部恢复、逐原 SHA 核对并消费。
它们不是从不含这些行的原 64 reused quarters 中猜取。

每行均核 SC.18a：整个原闭行及其保存中点都在同一 candidate cubic，
并使用同一 exact repair offset。所有分母门、whole third jets 和
中点 jets 是该同一 row 的原件。没有用另一 candidate 片的中心值搭配本片 remainder。
完整真实 $dr$、Hermite 片及原 scalar partition 的公共交集均已付。

对 128 个物理测试模，所有有限 Laurent 乘积及指数 Taylor
$P=32$ 的无限尾完整保留。真实角的三阶余项使用
$|e^{4il\psi}|=1$，未把它升级为 Wiener norm 等于 1。
普通径向导数与除以阶乘的 Taylor 系数各按 SC.13–20 转换。
$\beta,\gamma_{\rm rad}$ 的径向变化在所乘模型中，未当常数提出积分。

临时逐组审计总 32555737 B，32 个有序 receipt 的摘要为
`55a02902facc975a51ad13b054def6b88a03b5dbb2d45b3a1f98e22d516982a8`。
这些新逐行数组没有上传 artifact 或 Release；完整小结、全 signed 参数模型、
准确覆盖、输入身份和实际误差仍永久保存在本节所链原件中。

## 5. 完整 signed 参数模型的实际球

以下全部球逐字抄自原科学结论，不以近似十进制替代认证端点。

| 量 | 原实际完整球 |
|---|---|
| $\|a_0\|_{97}$ | `[3.8443257043572407713117079164286365336141607229502708733e-13 +/- 3.87e-69]` |
| $\|a_1\|_{97}$ | `[6.4486497895498052989103223260617322028799104315233270938e-13 +/- 3.32e-69]` |
| $\|a_2\|_{97}$ | `[0.00039863363403342862603657636681598269491281540485539599755 +/- 4.16e-60]` |
| $\varepsilon_3$ | `[1.2490481660908242100290177215511805720564429544433863530e-27 +/- 2.34e-83]` |
| $B_{\rm known}$ | `[3.8443257050419816041516922171654266930791477245352640214e-13 +/- 6.06e-70]` |

第 96 槽的三组 signed scalar-mean coefficients 为：

| 量 | 原实际完整球 |
|---|---|
| $\delta^{0}$ coefficient | `[+/- 2.28e-15]` |
| $\delta^{1}$ coefficient | `[-2.9e-15 +/- 4.96e-17]` |
| $\delta^{2}$ coefficient | `[-1.18116087839e-7 +/- 5.58e-19]` |

因此，已知完整参数模型采用原成功计算
$$
 B_{\rm known}
  =\|a_0\|_{97}+d\|a_1\|_{97}+d^2\|a_2\|_{97}
       +\varepsilon_3 .
 \tag{SCA.6}
$$
表内的 `uniform_known_parameter_model_norm` 已包含 $\varepsilon_3$。
SCI 还保留三组 body、中点/端点指数尾及所有输入球。
体积分三阶径向误差的独立诊断是：

`[4.4852653707691546356099684477149009634125968134759012267e-13 +/- 3.61e-69]`.

这是已嵌入 signed coefficients 的误差诊断，不能再加一次，
也不能从某个总上界倒扣出来。该诊断的 triangle 上界可以比最后
相关 signed 向量的上界更宽；两者不是新的互斥数值门。
原数值范围明确保 `no_second_addition_of_embedded_errors=true`。

## 6. Selected cut、方向修补和真实左缺陷

原 cut 来自 candidate piece 5484；base65 与完整 raw193 的身份已经逐值核对。
$Z_{\rm can}$ 的 joint $\mathcal A_0$ 修补费只付一次；
本实现逐 amplitude 的 conservative box 放大也明确保存。
原 cut 的 low-entry verdict 没有被改写。

| 量 | 原实际完整球 |
|---|---|
| base $|m_0|$ lower | `[3.2072027189669122767781750877029579316059709854337727674 +/- 2.64e-56]` |
| selected $|m_\delta|$ lower | `[3.2072027189665844672571191735976007552701844233845934295 +/- 4.52e-56]` |
| complete $j_-$ | `[0.98666571708711604408694316042836669664430104890619481247 +/- 2.53e-57]` |
| complete $j_+$ | `[1.0133342829128839559130568395716333033556989510938051875 +/- 3.26e-56]` |
| complete $|\mu|$ bound | `[0.0032780951872517891596706818953105350058465896299141800000 +/- 1.44e-59]` |
| complete shape $\mathcal A_0$ bound | `[0.59799442844849221087676367517174781684504868646107540000 +/- 1.84e-58]` |
| joint canonical repair once | `[2.2920000000000000000000000000000000000000000000000000000e-16 +/- 3e-76]` |
| conservative coefficient-box joint majorant | `[4.4235600000000000000000000000000000000000000000000000000e-14 +/- 3e-74]` |
| $D_{\rm target}$ | `[5.8573229241624517130759717182349570795978699875003519910e-9 +/- 4.32e-65]` |

SC.21–22 的 multiplier 差只作用真实 odd96 测试；
独立 scalar mean 测试保持完整，不额外乘 $\alpha$。
因此
$$
 E_{L,\delta}=E_{L,0}+D_{\rm target},\qquad
 Y_L^\delta\le Y_L+10d .
 \tag{SCA.7}
$$
实际 selected 左缺陷和完整 known 左 shift 分别为：

| 量 | 原实际完整球 |
|---|---|
| $E_{L,\delta}$ | `[6.2854944232106525775375716449632019773224256011298802831e-9 +/- 9.89e-66]` |
| $10d$ | `[1.0000000000000000000000000000000000000000000000000000000e-9 +/- 3e-69]` |

新已知积分没有让 $Y_L^\delta$ 或完整未知 $y$ 消失；
body、left、outer 三条真实误差仍须同时付费。

## 7. 原 Gram 误差的准确单位与全部非线性项

原 `complete_Gram_HS_uppers` 的 body 值已经是 norm，
本次直接读取；原 endpoint `Gram_trace_uppers` 则是平方 norm，
在严格非负 gate 后取平方根一次。四端 Gram 的量纲不混用。
formal ordinary residual 使用 $r_0^*$，不再增加同一个 Hessian Gram 费。

记 $D,Q,E_L,E_R,Z_B,Z_m$ 为相应完整上界。本次保
$$
 Q\le \gamma_+\|z_{B,\theta}\|_{\rm HS}
            +\beta_+\|z_C\|_{\rm HS},
 \tag{SCA.8}
$$
其中 $z_C$ 含完整 mean；并沿原同球二次余项付 $13\rho Q$。

| 量 | 原实际完整球 |
|---|---|
| $D$ | `[0.0015465793004759426780873818467653024195000000821397595656 +/- 4.31e-59]` |
| $Q$ | `[886.98934496575707415360313522320860342696568104527728485 +/- 2.04e-54]` |
| $\|z_{B,\theta}\|_{\rm HS}$ | `[155.11803879746800132954438083227925454000002146434868773 +/- 2.43e-54]` |
| $\|z_C\|_{\rm HS}$ | `[1.5678043960240697128586135137522786252000001792329476549 +/- 9.06e-57]` |
| $E_{L,0}$ | `[4.2817149904820086446159992672824489772455561362952829215e-10 +/- 3.07e-66]` |
| $E_R$ | `[1.0705663743994713389061710823943489734980675022153556245e-40 +/- 2.31e-96]` |
| $Z_B$ | `[3.5661407095496135401752219745818316087507299291606855104e-26 +/- 3.34e-84]` |
| $Z_m$ | `[7.1147408009358014146416082871548739171623118634231434726e-11 +/- 3.92e-67]` |

当外端 signed affine 暂未计算时，修补中心 A.15 的
$r_{D,+}=1.3\,10^{-15}$、$r_{m,+}=2.05\,10^{-19}$
给完整
$$
 E_{\rm out,known}=Z_Br_{D,+}+Z_mr_{m,+}.
 \tag{SCA.9}
$$
实际球为：

`[1.4585218641964752729239441964689769415852303130931203608e-29 +/- 1.72e-85]`.

其原 $f_B$ 域为 $2^{-60}$，两端 height/mean 规格保留。
这里不是未修补中心的更小 affine 数，也不以小 $\gamma$ 删除该常数项。
若后续沿原已对全 $f_B$ 球统一的界使用，不重复加入同一 height 改变；
其他独立 height、span、$\lambda$、waist 和 matching 行仍按原接口另列。

## 8. 两个完整 posterior：整行选择，不拼系数最小值

每个帽输入域分别评估七个 complete priors：原 existence 球加六个 RW
完整 weighted 候选。对每个候选先得到同一完整
$(Y,Y_L^\delta,Z_R)$，再付
$$
 E_{\rm unknown}
 =(D+13\rho Q)Y+E_{L,\delta}Y_L^\delta
       +(E_R+0.006Z_B+0.00075Z_m)Z_R .
 \tag{SCA.10}
$$
原 shared-node value jumps 已精确为零；这里没有遗漏一个非零 jump 费用。
选择比较最终保存的 `complete_unknown_error` 的 outward upper，
随后保留该同一候选的全行。全部七行的 temporary audit 摘要为
`c99e908db7265b0209fbf74ff058976f032e77e902731dcd086a3561cebd6d91`。

两域都选择 RW weight $3/4$，完整字段如下：

| 完整量 | 原完整帽域 | tail 输入子域 |
|---|---|---|
| physical $\gamma$ domain | `[1.0000000000000000000000000000000000000000000000000000000e-9 +/- 3e-69]` | `[7.8125000000000000000000000000000000000000000000000000000e-12 +/- 3e-71]` |
| whole selected weight | `3/4` | `3/4` |
| $Y$ | `[4.4749301670528893293674053795395312714022226451480904290e-6 +/- 2.60e-62]` | `[4.4749301670528893293674053795395312714022226451480904290e-6 +/- 2.60e-62]` |
| $Y_L^\delta$ | `[2.3070535616987479618111455752183423630025243878064398418e-7 +/- 3.57e-63]` | `[2.2328802836242851139379446483491913021754665977376190565e-7 +/- 8.50e-64]` |
| $Z_R$ | `[9.9000000000000000000000000000000000000000000000000000000e-10 +/- 1e-69]` | `[9.9000000000000000000000000000000000000000000000000000000e-10 +/- 1e-69]` |
| formal + nonlinear body | `[1.6172023409546753009461230021857502549682970902138041832e-7 +/- 2.34e-63]` | `[1.6172023409546753009461230021857502549682970902138041832e-7 +/- 2.34e-63]` |
| left defect error | `[1.4500972296105753499335648826285643259688345122017834093e-15 +/- 1.37e-71]` | `[1.4034756570417464298097150341389112675977637144421229646e-15 +/- 4.06e-71]` |
| outer feedback error | `[5.2826950446948537332472088885155296308663118298425337234e-23 +/- 1.64e-79]` | `[5.2826950446948537332472088885155296308663118298425337234e-23 +/- 1.64e-79]` |
| complete unknown error | `[1.6172023554556481253213809710067724059748292014551123918e-7 +/- 2.57e-63]` | `[1.6172023549894323996330917697682739210782986177444044142e-7 +/- 2.91e-63]` |
| complete affine97 upper | `[1.6172061997813531673031309748854092189288146750224838248e-7 +/- 1.62e-63]` | `[1.6172061993151374416148417736469107340322840913117758472e-7 +/- 1.28e-63]` |

对于该实际选中行，global body $Y$ 仍由原 existence 支
$\rho\sqrt{R-L}$ 控制；原 RW weight 的完整末端因子并未给出更小的
whole-cap $Y$。这解释了两域的 body 误差球完全相同，
而减小 $\gamma$ 仅改变本次选择中的 left 项。
这不是把 whole radial body 误差声明为零，也不说明未知实际范数必然大。

最后本次完整 affine97 使用
$$
 \|b_\delta^f\|_{97}
 \le B_{\rm known}+E_{\rm out,known}+E_{\rm unknown}.
 \tag{SCA.11}
$$
表中最后一行正是这一完整和；已知模型的强烈 signed 抵消
没有消去 formal/nonlinear remainder。

## 9. 全部 20 个实际门

| 序号 | 原实际 gate | verdict |
|---:|---|---|
| 1 | new source arithmetic and complete SC parameters are immutable | PASS |
| 2 | published SA7a and SC18a plus all original small receipts are exact | PASS |
| 3 | same full7908 original physical cover and32 slice plan retained | PASS |
| 4 | all four omitted original pilot scalar rows retain their original midpoint jets | PASS |
| 5 | all five original shards and the complete exact canonical centre are unchanged | PASS |
| 6 | old complete formal field endpoint and value certificates have the same object | PASS |
| 7 | all32 complete original slices and every unchanged array receipt were checked | PASS |
| 8 | all7908 canonical scalar rows were consumed once with all four pilots | PASS |
| 9 | all7908 candidate pieces include the same original saved midpoint | PASS |
| 10 | all common integration intervals use the true complete radial measure | PASS |
| 11 | all original shared-node values agree exactly across the full trial | PASS |
| 12 | complete physical128 moments all means and97 input columns retain every exponential tail | PASS |
| 13 | all body ordinary third remainders are embedded in the full signed vector | PASS |
| 14 | raw193 canonical offset full mean and the entire selected angle domain are retained | PASS |
| 15 | both true endpoints use the unchanged original Hermite with exact first short extension | PASS |
| 16 | complete signed97 delta model retains quadratic jets and whole third error | PASS |
| 17 | body HS bounds and endpoint square-Gram bounds are converted with their true units | PASS |
| 18 | full affine both means whole-cap priors and original outer-height domain remain independent | PASS |
| 19 | all complete97 signed coefficients final error rows and serialized balls are finite | PASS |
| 20 | no successful old mathematics is rerun and no new arrays are uploaded or published | PASS |

这些门均为原实际 `passed=true`；没有根据静态代码或事后估计补写 verdict。

## 10. 原件恢复、stdout 保存与失败历史

实际恢复的 Git 输入为 23 个当前小文本（合计 451182 B）加
9 个 immutable 历史件，共 **32**。完整 input-receipt digest 为
`3371f188dc83dce9bbb4160f6cf97c163c4e7c9774ac97f61ac9377f95d10e12`。
8 个 Python AST 的完整 inventory digest 为
`41995a422e6bf2a92b14e22721005189b09199dc44e872d24e5cfac5d3947408`。
19 个数学身份的全部 key/SHA 在科学文件
`scientific_identity.input_sha256` 和 execution 的
`mathematical_input_sha256` 中逐字一致；没有仅按短 hash 或文件名认对象。

36 个恢复 artifact 都是旧的成功输入，实际压缩总 bytes 为
912764217；完整 artifact-receipt digest 为
`4dc9332372dc60fdf6be8f0eee369c4ef3dee2086a2fde65200e59d658515671`。
每个旧 native 的 exact member/bytes/SHA 与32组有序 plan 保留。
这些只在 runner 临时恢复；没有发布新数组 artifact。
新 artifact=0、Release=0、旧 producer/QR/Gram/Green/RW/积分重复=0。

完整科学 canonical bytes 已独立重建，精确得到
23672 B / `f0838341d4f661714328da407c9a45f7ef137c43e8ab1ca7f4adfc2b12e7893c`。
从最终 report 只删除 publication 前尚未发生的最后一条
23:29:53.963846 UTC README pull 行，与同一完整 science 重建
`SC_COMPLETE_SCIENTIFIC_PREPUBLICATION_V1`，
精确得到 **32824 B /
9f40e61659f7c3128bbcb9b76b7810002645924c618564d404d981255e3539d3**。
完整 prepublication process 则保原 marker receipt：
41178 B /
`3ff0a4ef6018a5f7bdbf578c14acfdaf395ca0e8c53c124fb6f3dcffa5948af7`。
最终 execution 已更新 publication capacity/live-index，
本篇没有声称仅由最终 execution 重新构造这个旧 process。

最后完整 body checkpoint 为 23607 B /
`2172edf36a82a6cd3fd09608502ddae3701c45128d9499cc08542b05a8f4efe3`，
cover 全32组/7908行；完整 known-model checkpoint 为 13360 B /
`e49fe61a638b109b5087c3970bad4e5888d83801f7790ce4eb5a7a8477cf2b5b`。
两者是实际原子文件完整重印的 receipt；本次审查使用已发布终态小件，
未再取 485160 B 的大 child log。该 log 仅保原 SHA256
`2c7e34bc1f903586895deeb8ff35c9c72c7bb9c0c565a0b4dede21085a5a7023`。

23 次真实 Git pull 后 README diff 全为空。
publication base topic 为 199345305 B，三个新小件后的 projected
topic 为 199421511 B，均为原 execution 的实际 metadata。
`final_topic_complete=false` 继续保留，它不是 child 成功与全部20门的反义字段，
而是完整总题尚未结束。

先前 SC1、SC2 失败结论仍保留：
SC1 在严格 legacy identity 输入门停止，0 个新完整 group/model；
SC2 通过旧输入后在首行 Laurent sequence constructor 失败，
首行未完成，不能把它写成“零新数学”或成功积分。
两份已公开失败记录分别保于 immutable commits
`8aae744cd3fa661e887f4b98156d8945a8994801`、
`1e87820289fbb56fcc46e1d7d642e9fe239ddd58`。
SC3 只采用已审的 schema 与 constructor 最小修复，
没有重跑任何先前成功的旧科学目标。当前完整 SC3 成功已锁，
后继消费者只读这些终件。

## 11. 当前已付范围与下一真实输入

本篇已经付的是同物理帽、同原伴随、同完整97输入上的 signed known
参数模型，以及给定原帽 prior 后的完整两域 affine 上界。
可将相应整行作为 [SA/SC 的完整边界 affine 输入](R133-supplement-exact-radial-subtraction-and-complete-known-cap-affine-moments.md)，
并沿 [SR 的同一实际 $f$ / fixed selected chart](R133-supplement-uniform-secant-cap-rows-and-complete-finite193-nonlinear-receivers.md)
接入；$\gamma$ 域和未知段不能错配。

原完整 core residual、未知 whole-core/右帽态、低/高 cut trace、
实际 chart $H^1$ 前提、两 physical means、waist、height 和全 matching
仍按各接口保留。科学结论明确维持：
`new_low_trace_gate_claimed=false`，
`new_core_selfmap_claimed=false`，
`new_full_BVP_inverse_claimed=false`，
`new_global_surface_claimed=false`。
本次结果不把已知 signed cancellation 转授为这些尚未完成的门。
