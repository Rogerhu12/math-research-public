# 实际完整材料 Haar 角矩：7ebb 首批

2026-11-26，Astra-larger-e4e2a2bf-20261126。公开[run45762076394/1](https://github.com/Rogerhu12/math-research-public/actions/runs/45762076394)阶段71已实际返回；完整原始紧凑值、所有严格尾有理字符串及命令保[第8卷](2026-11-26-public-actions-45762076394-1-part-008.md)。这次完整求积域已付，所请求的矩盒宽度尚未达到；有效包围仍可消费，不另设精度门。

## 1. 实际输入和完整范围

- 真实冻结候选仍是 `7ebb5f42b29e0979f7a84a93fb8decb0b45ae8ec2f8c713bed820a8adb33d37b`，来源[63/65/66](2026-11-26-actual-multiround-SOC-acceptance-and-own-first.md)，没有换父。
- 实际checkout `da56c9343ea9864c1a92703d44d6be1ea85e2dd3`，完整角矩源 `1d12d238cd1a034cc1261ea7f23b7c223693a3cbdd769d66c376e796b0770010`，数学定义/严格余项证明见[完整角矩接口](2026-11-26-true-material-Haar-angular-moment-input.md)及R691。
- M=160，完整工作角数Q=8192，周期导数阶12。所需2049个quarter orbits已实际全部完成，权重和8192；全部160个原core模保留，非截断材料平均。
- `complete=true`、`rho_positive=true`、`exact_integrals=true`、`finite_target_redefinition=false`、`all_modes=true`。目标是连续完整Haar积分，Q/导数阶只控制工作精度。

angular identity是 `0f21f1e2f6ec76b2df2ef50e2f255d1516cbb0bef404ffeb83b25215a00b213d`。当前工作moment carrier为 `haar-7ebb-fixed-target/moments.json`，实际SHA `027c36ae6f55a204a9636eabf2eda841609a784b823c76435d74bddce7f0c16f`；runner journal为 `haar-7ebb-fixed-target/moment-journal.json`、SHA `20ee7e2e4ea5b8259978c4fac8d99c7de0e54e573244b9f1ec5b40549b259833`。角矩和journal只留runner，完整源/参数可重建。

## 2. 精度责任如实保留

实际rho严格下界为

```text
805740143925879251048881692199694051923115374408117036301053130750571735278181325067648205178273839393/5070602400912917605986812821504000000000000000000000000000000000000000000000000000000000000000000000000
```

实际最大工作moment盒误差为

```text
345097249723866388913049805706531322520915763134899408771226157/1000000000000000000000000000000000000000000000000000000000000000000000000
```

请求为 `1e-14`，实际 `accuracy_reached=false`。完整的 inverse、inverse2 与phase alias-tail有理界保实际第8卷，未将高模/无限尾删去；以上不是简单有限角平均的舍入估计。没有以未满足请求宽度声称首批partial，也没有把有效但未达请求的盒改写成目标已达到。这次科学返回共 16.260672083000827秒，内部11.775609786000132秒，exit0、summary_errors/missing_outputs均空；首批报告66790 B / `763e1fb63be4e7894e30aae3d68c4f7aaea9ab09f79c88731329b28405027ca8`。

## 3. 接准确固定目标的完整求解

据这个真实完整carrier，接已刊c5a冻结接口和[新完整求解五源](2026-11-26-complete-frozen-Haar-amplitude-actions.md)。准确 $g_*$ 由实际7ebb场的完整材料Haar积分定义，随后保持不变；旧moving-mean的Phi/几何不作为新目标下降或新场证书。

当前选择新目标初始μ=.01，明确不是继承旧moving-mean末μ=.005。完整首方向1×256保全部原变量、均值残差、原H²、192曲率+幅度行、全部永久点和4.2/.9/1.01预算，使用完整原ray真回溯；没有声称Haar已具deep多轮SOC。初始和最终Phi必须由该同一新固定目标实际计算。冻结manifest/目标SHA、新方向/末场SHA仍等实际返回，不能用计划填入。

完整实际后继参数见[actual71后继](../computations/resume-20261126-Haar-after-actual71-steps.json)。只在新的候选确有低误差后再支付其完整连续metric/K/reach；准确目标接口和当前科学输入已就绪并继续执行，不以本角矩完成代替课题完成。
