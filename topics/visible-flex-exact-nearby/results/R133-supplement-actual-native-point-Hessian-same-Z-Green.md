# R133：原生中点 Hessian 接入同一 $Z$ 的完整有限 193 维 Green 实际结果

公开 [Actions run 43635487128](https://github.com/Rogerhu12/math-research-public/actions/runs/43635487128) 已真实完成。8 个门全部通过，child 返回码为 0。原 6391 个连续片、全部 projector 接口、腰 $0^-$ 约束、真实低 97 帽约束及独立 even mean 保持不变。

**本条首次把同一连续 $Z$ 的有限 193 维压缩响应负窗误差上界推进到 $1/200$ 以下。它仍不是完整无限维参数响应误差。**

## 1. 实际原件和计算范围

实际科学源码为 scripts/fourfold_codazzi_native_point_Hessian_cached_Green.py，SHA256
c5236ced736f8610f65ae37a197fa739aef80eecc32db45bb613449eecbd1714。
worker SHA256 为 b3171bd781313d436237a492ec7ef0690eff7a9b0738850db181a2a869900f61，
287 项 manifest SHA256 为 f5cdddf72bde6dbd2785452811832a3d6109a242796943782954a6d98c21d18c。

目录：
notes/native_point_Hessian_Green_ci/run-43635487128-1-native-point-Hessian-cut-Green/。

| 原件 | 字节数 | SHA256 |
|---|---:|---|
| native/complete-same-Z-native-point-Hessian-cut-and-Green.json.gz | 3,996,581 | 7fcd5bec6763cb8ed84f7440fee568b2ec70adf804b610dd6cd368460a84ed66 |
| process.json，本次读取的仓库快照 | 9,889 | ad08b148fd2df4f8cb8b3f1cc72550b4cc9bb99fa51018c284dbc43dd5d419ab |
| evidence/complete-native-point-Hessian-cut-and-Green-summary.json | 25,633 | 2fbdebedd95572e4122ae25a0276b31e88138e4a5a162506c8e1d2d98be36d04 |

科学 native 用时 5.133069694 秒，worker 记录 child 用时 10.000706131 秒。没有重新计算任何 target、body 残差、帽格、Hessian 源格、Riccati、projector 或原 Green 源传播。本次只读取已成功的 64 原生点 Hessian native 41156aa8ac5b124b2ccca96e2f52b210edf1a3f5c170fdf839e66bf0602725b8，更新同一个右边界数值负荷，并按原正线性 Green profile 作有向缩放。

原已成的 7721 格主体 $Z$ 源与旧 jump、腰边界通道原样保留。

## 2. 同一边界对象的实际上界

本条固定原物理 $\eta_0$ 和 $\nu$，采用中心定义
440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47，
方向定义
6a71cb8109b095cd242823d181e7c1ef525355b9b90bf8c59f88668b68231d04。

原 quarter 全帽的同方向物理误差仍为
$\epsilon_{\mathrm{phys}}(w_0)<3.601796223643\times10^{-8}$；
新 Hessian additive 为
$E_H(w_0)<4.641143057402\times10^{-9}$。
结合原完整 Hessian resolvent 及 $Z_{\mathrm{even}}-w_0$ 的原完整误差算子费用后，

$$
\epsilon_{\mathrm{mov}}(Z_{\mathrm{even}})
<4.079795328961\times10^{-8}.
$$

真实 cut 输出为：

| 完整边界部分 | 严格上界 |
|---|---:|
| 腰 96 行 source | $1.121483070336\times10^{-15}$ |
| cut 96 个 odd 行 | $1.317287472280\times10^{-7}$ |
| cut 独立 even mean | $4.079815735966\times10^{-8}$ |
| cut 全 97 行 Euclidean 范数 | $1.379019669555\times10^{-7}$ |
| 同一已知输入的完整 high 输出 | $2.920495224265\times10^{-7}$ |

97 输入仍按原正交归一化，mean 没有附加非零 Fourier 的 $\sqrt2$ 因子。全部 14 个物理费用与六个真实边界错误保留；配套物理界按整套选择。未知输入的完整 moving 误差算子上界 $0.000146553004742$ 没有被特定 $w_0$ 的改进替换。

右通道采用的安全比例小于 $0.002525630678496$。分母是原消费者真实使用的正数值负荷的有向下端，绝非未知实际边界 defect 的下界。因此整条正线性 profile 的缩放合法。

## 3. 完整有限 193 维响应误差

在真实内主体 $[0,9/10]$ 上，有限 193 维误差为

$$
\|e_{193}\|_{L^2_rL^2_\phi([0,9/10])}<0.007490301792401,
\qquad
\|e_{193}\|_{C^0_rL^2_\phi}<0.060889190964764.
$$

完整安全负窗为

$$
\left[0,\frac{2383968743003}{10000000000000}\right].
$$

它包含同一背景的真实根，不把新背景的根位置免费包含在内。在这个窗口上，

$$
\|e_{193}\|_{L^2_rL^2_\phi}
<0.003509417445587<\frac1{200}. \tag{N.1}
$$

全部输入通道的负窗贡献为：

| 通道 | 严格上界 |
|---|---:|
| 完整同 $Z$ 主体源 | $0.003051713267954$ |
| 原 trial jump 的非负额外负荷 | $2.294290955931\times10^{-11}$ |
| 同 $Z$ 腰边界 | $2.820848755080\times10^{-12}$ |
| 同 $Z$ 真实右边界 | $0.000457704151969$ |

总界由原逐片同一正向解范数及真实 $dr$ 完整积分得到，不能只把这四个单独范数之和重新命名为原总值。每个连续片都保存完整来源，固定负窗切口在原覆盖内准确保留。

## 4. 真正剩余的无限维门

(N.1) 是完整有限压缩 BVP 对连续 $Z$ 的误差上界。它不证明真正无限维 $q_\nu-Z$ 满足同一门：未知高频解、body 双向反馈、真实帽 DN 的完整低高交叉及其全局 Schur 仍必须付清。已知 high 主体源和本条已知 high cut 输出均独立保存，没有被置零。

本结果也不把 $\delta=0$ 的中心或根窗口转授到非零 $\delta$、新 $\nu$ 或真正非线性背景。有限维 $1/200$ 门通过，只为后续完整反馈留下预算；真正参数 Schur 在 native 中仍为未证。

过程保存 4 次真实 pull 后的 README 检查，差异全部为空。最后读取提交为
89564f4c7de68dd2a25674daf509896c62519c81；使用已单独读取的规则提交
ee26c0a65a2e63c15f2ccfba6714181584416542。后续消费 artifact 过程必须记录其真实字节 SHA，勿用上述仓库出版快照代替。
