# m3：原 mean1168 下完整 lift 的角度二阶 metric 诊断

维护会话：Astra-held10-1b6d88ec-20261120。

本条只读已接受的 newg-wide-lambda0p002-m24-linear 场，未增加 lambda、
未重解前缀或尾。目标是给尚未支付的连续角度误差界提供实际导数尺度，
不把节点最大值或有限 FFT l1 当作真实连续上界。

新增脚本 scripts/resume_m3/audit_metric_angular_second_jet.py，使用原
physical quintic、完整 exact lift 与 s 依赖角图，固定原 mean1168。
评价角网格改变时不改变均值。参考第三角导数没有用有限差分：

    Γ'''(u) = −(κ_u+iκ²) exp(iφ).

原 core.evaluate 已给 κ_u；合并真实 material→psi 链式法则、原
Fourier basis 的解析三阶导数，以及 exact-lift 系数 1，恢复完整
g.p3。对角图 theta=psi−e(s)sin(3psi)/3，有

    rho_pp = 9(1−rho),
    v_pp = −9v−2(rho_p/rho)v_p−(rho_pp/rho)v.

据此恢复 U=F_s、V=F_theta/a 的一阶和二阶 psi 导数。相对 Gram 的
三个二阶导数分别为

    2(|U_p|²+U·U_pp),
    U_pp·V+2U_p·V_p+U·V_pp,
    2(|V_p|²+V·V_pp).

## 实际执行

~~~bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 python -u \
  "$TOPIC/scripts/resume_m3/audit_metric_angular_second_jet.py" \
  --source-run "$WORK/newg-wide-lambda0p002-m24-linear/run.json" \
  --physical "$WORK/newg-wide-lambda0p002-m24-linear/physical.npz" \
  --mean-nodes 1168 --angular 1168 2336 \
  --out "$WORK/newg-wide-m24-angular-second-jet.json" \
  > "$WORK/newg-wide-m24-angular-second-jet.log" 2>&1
~~~

实际 exit 0，1410 个物理 s 断面。两个网格都得到：

| 指标 | 实际有限值 |
|---|---:|
| 相对 metric operator 最大值 | 5.449318619907024e-7 |
| 解析二阶角导数 operator 最大值 | .0029356859387988533 |

二阶角导数峰在 s=.13976236085430432、psi=.08607103160519981、
theta=.05867047219465865，三个矩阵分量为
[.002931214835492635, −.00011465093910104085, −.0000042680136114192635]。

2336 网格的二阶导数三个分量有限 FFT l1 为
.0038046154591313878、.001496516325166814、.0014090500952139847。
解析二导与对同一 metric 节点作 DFT 二导的最大差，从 1168 网格的
8.838448956169278e-8 降到 2336 网格的 4.529221018145704e-9。
这个对照是有限求值检查，不是未采频尾的界。

对 N=1168 的角线性插值余项 h² sup||E_pp||/8 而言，sup||E_pp||<.12
会给约 4.34e-7 的余项；当前实际节点最大二导约小 40 倍。因此这个
条件界在数值尺度上有余量，但 **sup<.12 尚未证明**，径向区间也未付。

本诊断仍是原数学 jet oracle。geometry 分支的显式新 C² 图与真
primitive 的 Gram 传递 ≤3e-8 目前只覆盖 lift=0 的整段 bridge；
不能把这一数直接加在含 lift 的整个前半 prefix 上。全 prefix 的
真实 core/lift、profile 值接口、均值 primitive 和共享 Hermite 余项
仍须各自绑定，不能混同原 GL6 高度和真积分。

## 来源

| 对象 | SHA256 |
|---|---|
| 新解析二阶诊断源 | 54b5255edd9c1d7efc2d81dda7043308de35a0694e715d421b25724cd7fe1653 |
| 原 M24 run.json | c44b6fd2fbb13cc9ce0451cc6ab1d3c06521de0622de27190bde94c4c550462a |
| 原 M24 physical.npz | f2e22fe19bb0b6fdeff79c4fa99363d9be6cbb1ef382fd882679a2b717a3030d |
| 实际短输出 JSON | 197dbb721c057974bc79d805c8463d0287f3821f24526e5a2be507228fe5efba |

