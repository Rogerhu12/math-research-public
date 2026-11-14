# R133：64 个真实缺失中点的原生点值与同一方向 Hessian 实际验收

本条记录公开仓库 Actions [43635264409](https://github.com/Rogerhu12/math-research-public/actions/runs/43635264409) 的实际完成结果。只更新同一个物理帽提案方向 $w_0$ 的 Hessian 源上界。完整 PDE 逆、未知高频反馈和真正的参数响应尚不由本条推出。

## 1. 实际运行与原件

科学源码为：

- scripts/fourfold_codazzi_missing_native_point_Hessian.py，SHA256 `5845549dd474d744be2dae5ef3f0c608ea61eb7a2c97c6cedebd3b73d0b159e5`。
- worker SHA256 `a934d2ad4afa6fae2d56f6a4202662792771618fc564699ff1fb67d601503398`。
- 193 项输入 manifest SHA256 `a4ca896cc3eb2b0b3f02a7249aec49deabe3920ee9e50f0b59f984c4661f60f0`。

实际 child 返回码为 0，26 个数学门全部通过。科学 native 记录用时 52.438332593 秒，worker 记录 child 用时 60.001887675 秒。它们记录不同范围，不能相互替换。

目录为 notes/missing_native_point_Hessian_ci/run-43635264409-1-missing-native-point-Hessian/。

| 原件 | 字节数 | SHA256 |
|---|---:|---|
| native/complete-missing-native-point-Hessian.json.gz | 7,797,760 | `41156aa8ac5b124b2ccca96e2f52b210edf1a3f5c170fdf839e66bf0602725b8` |
| process.json，本次读取的仓库过程快照 | 24,048 | `519b7e39ea129daaf445afec85720c0d935f73630bd5c1ad9fbdf7c4faedb5aa` |
| evidence/complete-missing-native-point-Hessian-summary.json | 29,147 | `f388ab7d61c79b10cc52139d854a099af8d675067f6d4b80fc09fc9e20a98754` |

完整 native 保留为 4 个原字节分片。上述 process 是仓库快照；后续消费者若读取 Actions artifact 的过程，应保存其真实字节身份，不将出版记录追加前后的两个过程 SHA 混同。

## 2. 只补原来缺失的点包络

原完整 7908 个 quarter 的 whole jets 不重算。原 7844 个已成功的中点残差不重算，先前由 Taylor 路径导出的 64 个包络也完整保留。

本次在相同实际标量 germ、相同原始 $\nu$ 和固定物理 $\eta_0$ 上，计算确实缺失的 64 个原生中点。每个 $0,1,2$ 阶点值球与原 whole 球、已成 Taylor 点球取交；任何空交都会使数学门失败。第三阶仍使用原 whole 第三阶包络。因此这是同一个标量对象的新包络，没有修改候选、trial 或原整格误差。

实际新增为：

- 64 个原生中点取值；
- 64 个对应的完整有限频带残差消费；
- 16 个受影响的原局部 Hessian 行。

其余 1325 个局部行按原字节身份复用。全部 1341 个原局部行、1977 个 trial 交段、7908 个 quarter 覆盖以及独立 even mean 均由实际门核验。物理 Gram、真实径向长度、joint Wiener 余项和 193 倍 repair 费用保持原合同。

## 3. 实际完整上界

在原四种完整分解及原完整界之间比较后，本次得到同一 $w_0$ 的 Hessian additive

$$
E_H(w_0)<4.641143057402\times10^{-9}.
$$

先前 Taylor 结果为

$$
E_{H,\mathrm{Taylor}}(w_0)<5.884046519508\times10^{-7}.
$$

新的 tight ordinary 两个源范数分别为

$$
O_B<1.394879998675\times10^{-10},\qquad
O_C<1.284201134269\times10^{-10}.
$$

这里直接使用普通源表示，其 divergence 两项为零；完整四源表示仍另存并整体比较。没有逐分量拼接不同分解来制造更小结果。实际整体选择给出的物理 Green Hessian 源小于 $4.623320319864\times10^{-9}$，再乘原完整 Hessian resolvent 后得到上面的 additive。

同一 $w_0$ 的完整物理帽误差继续按

$$
\epsilon_{\mathrm{mov}}(w_0)
\le H\,\epsilon_{\mathrm{phys}}(w_0)+E_H(w_0)
$$

消费，原 $H<1.003854964897$ 保留。它不能替代未知输入的完整误差算子。对于真正已知边界方向 $Z_{\mathrm{even}}-w_0$，仍须乘原完整 moving 误差算子；全部 14 个物理费用、6 个原边界错误、97 个正交输入、独立 mean 和已知 high 输出均继续保留。

## 4. 真实 pull 与范围

过程记录 4 次真实 pull 后的根 README 与本题 README 检查，全部差异为空。最后读取提交为 `fcf2f3f49810bd411a6044b69f768f1f3ddf04d9`，采用已单独读过的规则提交 `ee26c0a65a2e63c15f2ccfba6714181584416542`。

本条仅授固定物理 $\eta_0$、原始 $\nu$、同一连续修补 M32 中心与同一 $w_0$ 的完整特定方向 Hessian 源。有限 193 维 Green 误差需由后继独立消费者读取本次 native 后计算；完整无限维帽端反馈、负区高频逆、低高 Schur 及非零参数背景转移仍保留。
