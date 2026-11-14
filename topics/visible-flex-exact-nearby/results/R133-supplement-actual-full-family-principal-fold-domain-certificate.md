# R133：实际全参数解析主部折叠与宽条带逆的已执行证书

2026-11-14。状态：公开实际16门全部通过。依据
[解析折叠证明F1–23](R133-supplement-actual-moving-analytic-principal-fold.md)，
现在可以使用同一实际全参数坐标变换、完整复逆矩形及新宽度的全频J界。

## 实际运行和原字节

公开 [Actions 43602612900](https://github.com/Rogerhu12/math-research-public/actions/runs/43602612900)
已success，child returncode=0，调用实际wall=0.21436293599999345秒。
Python3.12.14、python-flint0.9.0，Arb256bits。
10个固定输入逐个核全SHA，未重跑原germ、response或transport。

事件与实际科学checkout同为
`7b31f6eec5d6ebb53b966e7bd451ebb193fdd013`。

| 原件 | 完整SHA256 |
|---|---|
| 新完整native | `9300be45949cba94115511bf77d025a82e39c78d491ba77de916d7a96902fffd` |
| 实际consumer process | `e04f2aafdcb8b7fd5628754523b5704a2d25ea57f389ddd2026de08d32517107` |
| 新数学source | `2c680f47bc5209bd78f0643d7d425485bc597f05ad96c932109d93f2b26b2ab6` |
| 新CI driver | `383a1d9cfeabdb08151d3e2e7eae980a2f998294f3c857fd7c13b86adf127991` |
| 10输入manifest | `77e9457a7d2fed523c47e8e7f67d51fc5e14ade859c4c42abad3bdfd46f5962f` |
| 解析证明F1–23 | `c191e654a5fe2d48098195f8d6a7d2909161f0254efc047f761481194bcd224b` |
| 原实际joint germ | `397f9b428c787823994f8c849ad7d1f9209220c3c6e8907b38be562b3cbc9864` |
| 原完整moving root budget | `10ff6db82cece6c72ae8a6726c07c188922cf6b307f5af5f50a691ade0abb33f` |

[完整实际process与16门](../notes/current_moving_principal_fold_ci/run-43602612900-1/consumers/process.json)
原样保留。新worker SHA
`88037ff0e20ad6bd43c0cb15b04f23b16df489f693711bad3556c5875612376c`；
workflow SHA
`fa9f0781b373c86035de3a2c838697ee3a61298b53223c88be267136bcfd5fcf`。

## 真正的全参数域和坐标

固定原物理eta0，修复定义440866a3…和完整原193方向；
全复参数圆盘 |delta|≤1/100000000。基底M32、方向M96和产品band192全部保留。
所有径向域在原piece2549内，原紧支参数bump在整个root片准确为零。

以rho=rstar−r、e=−d、D=partial_rho−e partial_phi。
原两个真实特征foot流给
X=(Splus+Sminus)/2、
A=3(Splus−Sminus)/(4rho^(3/2))、
T=−rho A^(2/3)。
奇偶性使A为rho解析函数，正实gap固定唯一cube-root分支。
准确主部变成mu(partial_T²+T partial_X²)，其混合项为零。

从原moving条带1/1024按完整频率128和384分别扩大系数envelope到1/64；
不是无费用外推。构造半径R=9/1000000，flow输出条带3/256，
真正反解定义于
|T|≤81/4000000、|Im X|≤1/128，
其径向像 |rho|≤3R/4。
原 |rho|≤4/1000000、|Im phi|≤1/256 的完整积域在该反解矩形内。

反解fixed point准确为
rho_new=−tau/(9/2)+(T+(9/2)rho)/(9/2)，
phi_new=chi−(X−phi)；
径向余项的加号为已审的正确符号。

## 已执行域界

下列十进制均向安全方向放宽，精确Arb记录在原process：

| 完整量 | 实际严格界 |
|---|---:|
| Re a 的正gap | >9.689661640982 |
| a模 | <9.778607174755 |
| drift D0 | <0.898891583038 |
| drift_phi D1 | <3.595566332149 |
| drift_phiphi D2 | <29.625513819276 |
| flow位移M0 | <8.266039176480e−6 |
| 一阶flow差j | <3.236062058293e−5 |
| inverse角半径b0 | <2.479811752944e−5 |
| Re A的gap | >9.689345199186 |
| A模 | <9.778923616551 |
| A_phi | <0.001564562320 |
| T_phi | <4.403310464315e−9 |
| 完整principal D与1之差 | <6.472228837562e−5 |
| Jacobian模下界 | >4.530889644653 |
| mu模下界 | >20.530289739365 |
| inverse径向行norm | <0.106509367786 |
| inverse角行norm | <0.326278336185 |
| 旧角两幅principal矩阵H逆 | <1.000097093597 |

两inverse行都严格小于1/2，radial self-map与角条带余量全通过。
这些门覆盖实际analytic ODE构造的整域，未采样特征流来替代证明。

## 新宽度上的完整J

完整moving非mean算子A的逆J，重新在A_(1/128)上付费。
同一原65基底和193完整方向系数给：

| 完整量 | 实际严格界 |
|---|---:|
| eta_inverse | <0.797681384652 |
| L0 | <3.802900756013 |
| Neumann factor cJ | <0.758375785188 <4/5 |
| J同空间norm | <0.825332619571 |
| partial_phi J | <3.301330478284 |
| 新inverse像上的partial_rho J | <253948.498330 |

新J界适用于完整moving Wiener A_(1/128)、同宽weighted Fourier H0
与ordinary L2。原半径1e−5与inverse像之间的真实径向margin
为13/4000000，最后一行使用此margin而非旧半盘。

canonical |Im X|≤1/256的反像落在moving |Im phi|<1/128内。
这是新J所需的真实域；任意沿倾斜曲线的source norm仍须另外证明。

## 完整算子结构及后续

旧角导数保持为
Y=alpha partial_X+beta partial_T，
alpha=X_phi、beta=T_phi=O(T²)，
alpha²+T beta²=principal D。
原角primitive沿旧rho固定的闭曲线，原mean仍取原dphi measure；
根T=0处恰与canonical版本重合。局部切向一阶项准确有T²因子。

本结果完成实际principal fold和域/逆预算，尚未给两行根部连接、
完整mean/primitive/source的Airy变换norm、实际反射有限常数brootfin、
强4/3余项或非线性PDE分支。它们仍按原open主线继续。
