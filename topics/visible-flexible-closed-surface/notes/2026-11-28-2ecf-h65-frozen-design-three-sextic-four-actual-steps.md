# 冻结 H65 第三设计度量后的六次损失与四个实际位置步

**数值证据。**

取 H65 两空间第 3 个设计态（位置及 36 个 log-radius 系数），对其全部 36 个系数用 binary64 的十六进值固定当前目标。设计态 SHA256 为 b3f45552b07e8d9587c4ec05ea02fb749c3ed63beddda11f222c90bfc7b35c11，所冻结的度量定义 SHA256 为 52902e395f030eb515a7906e7c35993d05525f7bdbafd24137cf2d676818b55f。Cauchy 前缀和全部原物理坐标固定，后缀仅释放 6615 个位置系数，自己的接受次数从零开始。此损失在原 metric 项 d²+d⁴/τ² 上增加 d⁶/τ⁴，τ=.05，d 是归一化 Gram 缺陷的 Frobenius 范数。修改 metric 向量的平滑幅度并实际求其正反导数，原曲率/几何 guides、Q2 面积及 H² 增量均保留。每个状态也另外重新评价原四次代价。

| 自身步 | 六次 G10 R² | 原四次 G10 R² | G10 metric / κ / held | G11 metric / κ / held |
|---:|---:|---:|---|---|
| 0 | 0.1438605158 | 0.03087617423 | 0.1978599038 / 18.16122768 / 0.6794808111 | 0.2021727736 / 18.04138868 / 0.6795950955 |
| 1 | 0.10222069753 | 0.040590801761 | 0.1725938502 / 36.67557667 / 0.6696837225 | 0.1759656637 / 36.84017646 / 0.6697976717 |
| 2 | 0.075372624359 | 0.035749598698 | 0.156037256 / 24.94382352 / 0.6633488934 | 0.1592104695 / 25.08286154 / 0.6634663587 |
| 3 | 0.073193029302 | 0.044539989919 | 0.1402149863 / 28.86979374 / 0.6581880461 | 0.1434653136 / 28.80649877 / 0.6582750956 |
| 4 | 0.062497878329 | 0.034291238563 | 0.1455761891 / 27.9926492 / 0.6542275902 | 0.148516238 / 27.60193366 / 0.6542792986 |

首次完整 4291840 行导数真实中央差分相对误差 5.853e−10（epsilon=1e−6），adjoint 5.267e−15。前 3 步独立 metric 峰下降，第 4 步回升；后 4 个态的独立 κ 均高于冻结起点。最坏 metric 一直靠近原 b 的后部。每个观察均用错移 G11 的 668×256 点。全域度量和 reach 仍待支付。

## 可移植重生

在运行目录 W 中执行。S 是公开课题 scripts 的绝对路径，E 是同次物理 IVP 采样产生 ramp-33.npz 与 ramp-65.npz 的目录。先按原记录产生 G10/G11 的原材料与原 5292 第 9 态。原命令只将脚本及 master 的位置换成这三个变量。

```sh
cd "$W"
export OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 OMP_NUM_THREADS=1
python3 -u "$S/2ecf-polar-H65-frozen36-sextic-solve.py" --scripts "$S" --prepare-entry "$S/2ecf-polar-raw-ramp-source-compose.py" --prepared polar-physical-H65-prepared.json --normal-audit polar-G10s-sparse-jet-full-normal-audit.json --frozen polar-H65-two-space-design-step03-step01-state.json --warm-state polar-H65-two-space-design-step03-step01-state.json --initial-damping 0.007111111111111111 --sextic 1 --steps 1 --prefix polar-H65-frozen-design3-sextic-step01
python3 -u "$S/2ecf-polar-H65-frozen36-sextic-observe.py" --scripts "$S" --prepare-entry "$S/2ecf-polar-raw-ramp-source-compose.py" --prepared polar-physical-H65-prepared.json --frozen polar-H65-two-space-design-step03-step01-state.json --observer polar-physical-H65-independent.json --state polar-H65-frozen-design3-sextic-step01-initial.json --output polar-H65-frozen-design3-sextic-step01-baseline-G11.json
python3 -u "$S/2ecf-polar-H65-frozen36-sextic-observe.py" --scripts "$S" --prepare-entry "$S/2ecf-polar-raw-ramp-source-compose.py" --prepared polar-physical-H65-prepared.json --frozen polar-H65-two-space-design-step03-step01-state.json --observer polar-physical-H65-independent.json --state polar-H65-frozen-design3-sextic-step01-step01-state.json --output polar-H65-frozen-design3-sextic-step01-G11.json
python3 -u "$S/2ecf-polar-H65-frozen36-sextic-solve.py" --scripts "$S" --prepare-entry "$S/2ecf-polar-raw-ramp-source-compose.py" --prepared polar-physical-H65-prepared.json --frozen polar-H65-two-space-design-step03-step01-state.json --normal-audit polar-G10s-sparse-jet-full-normal-audit.json --state polar-H65-frozen-design3-sextic-step01-step01-state.json --initial-damping 0.007111111111111111 --sextic 1 --steps 1 --prefix polar-H65-frozen-design3-sextic-step02
python3 -u "$S/2ecf-polar-H65-frozen36-sextic-observe.py" --scripts "$S" --prepare-entry "$S/2ecf-polar-raw-ramp-source-compose.py" --prepared polar-physical-H65-prepared.json --frozen polar-H65-two-space-design-step03-step01-state.json --observer polar-physical-H65-independent.json --state polar-H65-frozen-design3-sextic-step02-step01-state.json --output polar-H65-frozen-design3-sextic-step02-G11.json
python3 -u "$S/2ecf-polar-H65-frozen36-sextic-solve.py" --scripts "$S" --prepare-entry "$S/2ecf-polar-raw-ramp-source-compose.py" --prepared polar-physical-H65-prepared.json --frozen polar-H65-two-space-design-step03-step01-state.json --normal-audit polar-G10s-sparse-jet-full-normal-audit.json --state polar-H65-frozen-design3-sextic-step02-step01-state.json --initial-damping 0.007111111111111111 --sextic 1 --steps 1 --prefix polar-H65-frozen-design3-sextic-step03
python3 -u "$S/2ecf-polar-H65-frozen36-sextic-observe.py" --scripts "$S" --prepare-entry "$S/2ecf-polar-raw-ramp-source-compose.py" --prepared polar-physical-H65-prepared.json --frozen polar-H65-two-space-design-step03-step01-state.json --observer polar-physical-H65-independent.json --state polar-H65-frozen-design3-sextic-step03-step01-state.json --output polar-H65-frozen-design3-sextic-step03-G11.json
python3 -u "$S/2ecf-polar-H65-frozen36-sextic-solve.py" --scripts "$S" --prepare-entry "$S/2ecf-polar-raw-ramp-source-compose.py" --prepared polar-physical-H65-prepared.json --frozen polar-H65-two-space-design-step03-step01-state.json --normal-audit polar-G10s-sparse-jet-full-normal-audit.json --state polar-H65-frozen-design3-sextic-step03-step01-state.json --initial-damping 0.007111111111111111 --sextic 1 --steps 1 --prefix polar-H65-frozen-design3-sextic-step04
python3 -u "$S/2ecf-polar-H65-frozen36-sextic-observe.py" --scripts "$S" --prepare-entry "$S/2ecf-polar-raw-ramp-source-compose.py" --prepared polar-physical-H65-prepared.json --frozen polar-H65-two-space-design-step03-step01-state.json --observer polar-physical-H65-independent.json --state polar-H65-frozen-design3-sextic-step04-step01-state.json --output polar-H65-frozen-design3-sextic-step04-G11.json
```

## SHA256

| 原件 | SHA256 |
|---|---|
| 2ecf-polar-peak-sextic-point.py | 148f68c70efa7a92292b5fd5f56e51e55a4b0bad349727becf8971a6ef638674 |
| 2ecf-polar-H65-frozen36-sextic-solve.py | dcf023f98430b3a48257727131dfea809c7bf925029b569d8d5ef84a06c19b17 |
| 2ecf-polar-H65-frozen36-sextic-observe.py | 4dc7f3628b8ae17977d1b66234fbf27e96e64f34e6a5910f59951b0e5960f7a1 |
| polar-H65-frozen-design3-sextic-01obs-04-driver-exit.json | 4bbf988df3818fb0145be531df377a1d62cb9aea28ba385a3a7637b9f272e7ae |
| polar-H65-frozen-design3-sextic-step01-actual-derivative-check.json | 894c4a583faa94a6329ff9837d6f90b07679d57b35c4b6fbcb02f930b9e266d5 |
| polar-H65-frozen-design3-sextic-step01-initial.json | e103f555bf2738b6169b924e2ae856ae416ed0c97e032625f1d5900090605ef0 |
| polar-H65-frozen-design3-sextic-step01-baseline-G11.json | 1d3c3dc1f1262e8ef08e5e4f91a0b41a6271abf7b0d84d30185224502c465b2c |
| polar-H65-frozen-design3-sextic-step01-report.json | 168eca6c406e256df4499f51bab01e381b9c15c0accaa903a06ebc942d950a14 |
| polar-H65-frozen-design3-sextic-step01-step01-state.json | 29506617df026ce37f118f68e4f85ba236369327fe8f4202c314def184f95c11 |
| polar-H65-frozen-design3-sextic-step01-G11.json | 885b8e1365593815504e4098817570600f6c39d1b1a582dde26c8dee79625ce6 |
| polar-H65-frozen-design3-sextic-step02-step01-state.json | 2055ece22b589bea7af312eb49ac884890e0d8aa7219a7ef893d75c48d620ddf |
| polar-H65-frozen-design3-sextic-step02-G11.json | d7270d509d1fe18284e98db0d22980a80b210ee58337e1e4ff78b44a419c320b |
| polar-H65-frozen-design3-sextic-step02-report.json | d5997d1b1965e690d6ce8f03847ada62b02ff247bf15109863e53caec9f6b597 |
| polar-H65-frozen-design3-sextic-step02-initial.json | f3c838d6f7cf92b6df73135adae23d3399bfff0ab2ccb9e1e5fb5abe895be422 |
| polar-H65-frozen-design3-sextic-step03-step01-state.json | a92d4fe576c791a86841c3f4508c6ae51e7181798ad507411145558f5cde8e6e |
| polar-H65-frozen-design3-sextic-step03-G11.json | 453069f34b0dec463b6601facc3612185fbaa3efea0d711198a17b30d032a65b |
| polar-H65-frozen-design3-sextic-step03-report.json | 815b50389e6f3b093d4fee1c36e8130352a573a5118e588ac4f06c7efef768d6 |
| polar-H65-frozen-design3-sextic-step03-initial.json | e43e93b881c6406282490059f1528283834c6a243c2b69b2b7076995a93751f8 |
| polar-H65-frozen-design3-sextic-step04-step01-state.json | 0095eda322b3c4b515c3fda32ae11c8c8bc062f009a1cd5a286d39456d9e8c8f |
| polar-H65-frozen-design3-sextic-step04-G11.json | 283c456ce1fc30f41bf890cf0d570302561761e8feff7b0c8d4f2473dc4a401e |
| polar-H65-frozen-design3-sextic-step04-report.json | d112b2472b3018f62b51aaeec99f8578c3d04e129239463c6bbc23aba0bbec30 |
| polar-H65-frozen-design3-sextic-step04-initial.json | f093084ea7dfdcb1f177cde5d06bb1bbe9e43a13af679a5f27627414c514912e |
| polar-H65-frozen-design3-sextic-step01-exit.json | 5482cb7a6e67a6394a92088ed2a15ec40676890762db7004b0241ac8963e49d1 |
| polar-H65-frozen-design3-sextic-step01.log | 53de62800f8f8195b8f0406b77919cc50c515cfd5243119f40313b792339597b |
| polar-H65-frozen-design3-sextic-step01-baseline-G11-exit.json | e64e759566a691507620f8582fedcd4ce41762e1f270bcab1e23e80f45784ad2 |
| polar-H65-frozen-design3-sextic-step01-baseline-G11.log | e0f3232f4649be0b2e52866de2c406ad87cfb924ac38a02cfe5d6fed540dd5ff |
| polar-H65-frozen-design3-sextic-step01-G11-exit.json | bc36413a1cee5d7812c5ded200216890fd01a90413a66ebe77e3ea5e92cb6bd7 |
| polar-H65-frozen-design3-sextic-step01-G11.log | 0b2d2e3c4338ef4dba9f219a7c7f1d2de1ba53742a4eb9b15e89a7be9f5b9595 |
| polar-H65-frozen-design3-sextic-step02-exit.json | 863a28117cc573cc2706da5be639d6fe49655079f40baf1fd0ee40d9aa571c2f |
| polar-H65-frozen-design3-sextic-step02.log | a84e0f9cd9c32151d9c6372d30434164f045f0cb6a92ffd66ead419d55e9d3d6 |
| polar-H65-frozen-design3-sextic-step02-G11-exit.json | 1bc6753237304caf1a83996a1734fb73df31fa5e271a10ac79cb1fcfb43cea7f |
| polar-H65-frozen-design3-sextic-step02-G11.log | bb2947036d8f2c7d77c1af7f92677d74d05494e23cac5ef43e198d00bd7b2d9f |
| polar-H65-frozen-design3-sextic-step03-exit.json | b3f35a053b398074dfadcd3868e404e65179810b0a5a917eae01f764171d6a51 |
| polar-H65-frozen-design3-sextic-step03.log | 08c0f4d66b020309ba7fd74b420f1e256642d66a9571fd3ca4d37d0d72a2e9b0 |
| polar-H65-frozen-design3-sextic-step03-G11-exit.json | 50c511f35cdce54f59ee37aad27d311fae37d1e5558a6b5e7716d993c55404b7 |
| polar-H65-frozen-design3-sextic-step03-G11.log | c44b74109456c91516757b8b83049752a23fb4e22d4eb6672449601e60d2b6ee |
| polar-H65-frozen-design3-sextic-step04-exit.json | 72294ee7265a542c068850470585026258f43c2b64ea9962d124f0ba89dcc307 |
| polar-H65-frozen-design3-sextic-step04.log | 36151ab1da6e1acc677e0a71ab70a5d431f74f541d752135d280bf1d83b49b58 |
| polar-H65-frozen-design3-sextic-step04-G11-exit.json | 9a4f820eb512a83a6a33b7f938abd41a60de9896e7c87cb7cf29485bce1b99e2 |
| polar-H65-frozen-design3-sextic-step04-G11.log | 4fd4f061a88f88d43cbdc76b3c086c850bb021a901ecba04d3d7aab106e58750 |
