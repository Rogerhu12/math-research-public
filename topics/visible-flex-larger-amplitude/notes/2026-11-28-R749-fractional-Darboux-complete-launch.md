# R749 — 实际非线性C²等距局部延拓及完整有理系数公开运行

会话 Astra-larger-e4e2a2bf-20261126。完整证明与三件可执行源原子刊出；实际run/job/系数检查返回均尚未观察，不把解析存在证明或源代码当真实运行。

## 已证明的精确范围

[完整R749证明](../results/R749-fractional-Darboux-exact-local-continuation-at-the-displaced-straight-wall.md)在真实R746/R747右圆弧材料、移到物理平直墙的入口二jet下，以z=v^(5/2)u将整个Darboux方程转为以纵向x为演化变量的解析非特征CK方程。正W²下bar g=g−dz²解析且平坦，完整平面展开给X,Y并逐条付全入口二jet，故真C²非C³解在一个正宽矩形严格同g，而非仅有限formal jets。一个同矩形适用于两端和θ∈[1,π/2]。

可将此真解用O(δ^1/2) C²小修改裁拼进原完整闭场，保全相位reach≥.106、D0<3.40、held>1.520、grip≥1.40与δE>0，θ∈[1.1,π/2]的更小真子带严格等距；裁拼区、剩下圆端与帽仍未付。宽度存在但本证明没有可用数值下界，也没有全域收敛或完成声明。

## 原完整公开运行

标准库Fraction计算，不调用本地科学。真实固定r_y=27/250、ε_y=1/2000、κ=20/3、z次幂5/2；两个独立h0=1和64。每支依次完整(x,v)次数(4,8)、(8,12)、(12,16)，逐元复算完整非线性Darboux余式；检查行0…xdegree−2/列0…vdegree，全部重叠有理系数逐字一致。有限系数和零余式不付解析半径。完整有理raw仅runner，完整summary/源身份/原参数/所有失败未知在main note。

```text
python -u topics/visible-flex-larger-amplitude/scripts/resume_20261126/r749_fractional_darboux_coefficients.py --orders 4 8 12 --radial 8 12 16 --heights 1 64 --raw "$RUNNER_TEMP/r749-exact-series.json" --summary "$RUNNER_TEMP/r749-actual-report.json"
```

公开workflow checkout main后真实pull/rebase并核两README，标准库默认Python，job上限30分钟；全6盒没有新增科学wallclock切断/早停。完整返回后发布器先metadata总量、正常pull/rebase、非快进即继续循环；全报告<100KB才提交。实际科学run/attempt/source/results直到官方和完整note返回才填写。GITHUB_TOKEN由Actions提供，不写用户凭据。

## 整件身份

```json
[
  {
    "path": "topics/visible-flex-larger-amplitude/results/R749-fractional-Darboux-exact-local-continuation-at-the-displaced-straight-wall.md",
    "bytes": 12953,
    "sha256": "f2664d80027548f0859bb15ae5cb7493d9a1e2ce96a1f9ef1c6fa563f1f566b5",
    "git_blob_sha": "9499932b2ae7d4399ed62b97491ffafbd5c501cc"
  },
  {
    "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/r749_fractional_darboux_coefficients.py",
    "bytes": 7441,
    "sha256": "d07afa956b4edb43c0da5e5458afa5e498f79d10f29a1f1d7e5b0e8ae81b61c6",
    "git_blob_sha": "a07404a8c70059fe34bad06637921bd904194c0d"
  },
  {
    "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/publish_r749_darboux_coefficients.py",
    "bytes": 5970,
    "sha256": "4c51351531b9abd217440e6cf6c843c786c3365dc4616df7ec780f2dc56e228c",
    "git_blob_sha": "049508a588b087893633ddbb102e39756de26e15"
  },
  {
    "path": ".github/workflows/visible-larger-r749-fractional-darboux.yml",
    "bytes": 2693,
    "sha256": "8f3f35b32107b07dbcbca4d49c5dbe15d9a8e15e32507d982a9ae97816f912e7",
    "git_blob_sha": "00c51ce846ffc625c2a77f0f8c489567a9199369"
  }
]
```

所有source已完整读过，实际字段当前null；不能借同形式旧数值。
